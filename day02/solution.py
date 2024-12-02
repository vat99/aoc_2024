from typing import List, Tuple
import re
from functools import reduce

class Solution:
    def part01(self, fname: str) -> int:
        lines = self.read_input(fname)
        return reduce(
            lambda acc, line: acc + (1 if self.is_safe(line) else 0),
            lines,
            0
        )
    
    def part02(self, fname: str) -> int:
        lines = self.read_input(fname)
        safe = 0
        for line in lines:
            if self.is_safe(line):
                safe += 1
            else:
                for i in range(len(line)):
                    if self.is_safe(line[:i] + line[i+1:]):
                        safe += 1
                        break
        return safe
    def is_safe(self, line: List[int]) -> bool:
        increasing = line[1] > line[0]
        
        # Check each adjacent pair
        for i in range(len(line) - 1):
            diff = line[i + 1] - line[i]
            
            # Check if difference maintains direction and is within bounds
            if (increasing and not (1 <= diff <= 3)) or \
                (not increasing and not (-3 <= diff <= -1)):
                return False
        return True

    
    def read_input(self, fname: str) -> List[List[int]]:
        result = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                result.append([int(x) for x in line.strip().split()])
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input.txt"))