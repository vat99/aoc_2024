from typing import List, Tuple
from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def search(self, total, nums, current) -> bool:
        # if total < current or (total == current and len(nums) > 0) or (len(nums) == 0 and total != current):
        #     return False
        if current > total:
            return False
        if len(nums) == 0 and current == total:
            return True
        elif len(nums) == 0 and current != total:
            return False
        else:
            return self.search(total, nums[1:], nums[0]*current) or self.search(total, nums[1:], nums[0]+current)
        
    def search_cat(self, total, nums, current) -> bool:
        if current > total:
            return False
        if len(nums) == 0 and current == total:
            return True
        elif len(nums) == 0 and current != total:
            return False
        else:
            return self.search_cat(total, nums[1:], int(str(current)+str(nums[0]))) or self.search_cat(total, nums[1:], nums[0]*current) or self.search_cat(total, nums[1:], nums[0]+current)

    def part01(self, fname: str) -> int:
        equations = self.read_input(fname)
        result = 0 
        for total, nums in equations:
            if len(nums) > 1 and self.search(total, nums[1:], nums[0]):
                result += total
            elif len(nums) == 1 and total == nums[0]:
                result += total
        return result
    
    def part02(self, fname: str) -> int:
        equations = self.read_input(fname)
        result = 0 
        for total, nums in equations:
            if len(nums) > 1 and self.search_cat(total, nums[1:], nums[0]):
                result += total
            elif len(nums) == 1 and total == nums[0]:
                result += total
        return result

    def read_input(self, fname: str) -> List[Tuple[int, List[int    ]]]:
        result = []
        with open(fname, "r") as f:
            lines = f.readlines()
            for line in lines:
                split_line = line.strip().split(":")
                result.append((int(split_line[0]), list(map(int, split_line[1].strip().split(" ")))))
        return result


if __name__ == "__main__":
    solution = Solution()
    #print(solution.search(83, [5], 17))
    #print(solution.search_cat(156, [6], 15))
    print(solution.part02("input.txt"))
