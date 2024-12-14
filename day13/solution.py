from typing import List, Tuple
from collections import deque
from functools import reduce
import re


"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

x_a = 94, y_a = 34
x_b = 22, y_b = 67
x_p = 8400, y_p = 5400

Each puzzle can be written as a system of equations:

(x_a  x_b)(b_a)   (x_p)
(        )(   ) = (   )
(y_a  y_b)(b_b)   (y_p)

we can just solve this with Cramers rule:

      |x_p  x_b|
      |y_p  y_b|
b_a = __________
      |x_a  x_b|
      |y_a  y_b|

b_a = (x_p*y_b - x_b*y_p) / (x_a*y_b - x_b*y_a)

      |x_a  x_p|
      |y_a  y_p|
b_b = __________
      |x_a  x_b|
      |y_a  y_b|

b_b = (x_a*y_p - x_p*y_a) / (x_a*y_b - x_b*y_a)    
"""

class Solution:
    def read_input(self, fname):
        grid = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 4):
                chunk = lines[i:i+3]
                #print(chunk)
                numbers = []
                for line in chunk:
                    numbers.extend(map(int, re.findall(r'\d+', line.strip())))
                grid.append(numbers)
        return grid
    
    def part01(self, fname):
        puzzles = self.read_input(fname)
        total_count = 0
        def solve(puzzle, token_limit):
            ax, ay, bx, by, px, py = puzzle
            det = ax*by - ay*bx
            if det != 0:
                b_a = (px*by - py*bx) / det
                b_b = (py*ax - px*ay) / det
                if b_a % 1 == 0 and b_b % 1 == 0 and 0<=b_a<=token_limit and 0<=b_b<=token_limit:
                    print(f"{puzzle} solvable: {b_a, b_b}")
                    return int(3*b_a + b_b)
                else:
                    print(f"{puzzle} not solvable: {b_a, b_b}") 
            else:
                print(f"{puzzle} not solvable")
            return 0
        for puzzle in puzzles:
            total_count += solve(puzzle, 100)
        return total_count
    
    def part02(self, fname):
        puzzles = self.read_input(fname)
        total_count = 0
        def solve(puzzle):
            ax, ay, bx, by, px, py = puzzle
            px += 10000000000000
            py += 10000000000000
            det = ax*by - ay*bx
            if det != 0:
                b_a = (px*by - py*bx) / det
                b_b = (py*ax - px*ay) / det
                if b_a % 1 == 0 and b_b % 1 == 0:
                    print(f"{puzzle} solvable: {b_a, b_b}")
                    return int(3*b_a + b_b)
                else:
                    print(f"{puzzle} not solvable: {b_a, b_b}") 
            else:
                print(f"{puzzle} not solvable")
            return 0
        for puzzle in puzzles:
            total_count += solve(puzzle)
        return total_count

if __name__ == "__main__":
    solution = Solution()
    #print(solution.read_input("sample.txt"))
    print(solution.part02("input.txt"))