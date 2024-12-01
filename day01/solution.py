# day01: calorie counting
from typing import List, Tuple
import re
from functools import reduce

class Solution:
    def part01(self, fname: str) -> int:
        column1, column2 = self.read_input(fname)
        return reduce(
            lambda x,y: x+(abs(y[0]-y[1])),
            zip(sorted(column1), sorted(column2)),
            0,
        )

    def part02(self, fname: str) -> int:
        column1, column2 = self.read_input(fname)
        col2_counts = reduce(
            lambda acc, x: {**acc, x: acc.get(x, 0) + 1},
            column2, 
            {}
        )
        print(col2_counts)
        return sum(
            map(
                lambda x: x * col2_counts.get(x, 0),
                column1,
            )
        )
    
    def read_input(self, fname: str) -> Tuple[List[str], List[str]]:
        column1 = []
        column2 = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parsed_line = line.strip().split()
                column1.append(int(parsed_line[0]))
                column2.append(int(parsed_line[1]))
        return (column1, column2)

if __name__ == "__main__":
    solution = Solution()
    #print(solution.read_input("sample.txt"))
    print(solution.part02("input.txt"))