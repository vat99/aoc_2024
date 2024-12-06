from typing import List, Tuple
from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def part01(self, fname: str) -> int:
        grid, start_loc = solution.read_input(fname)
        visited = set()
        visited.add(start_loc)

        def turn_90_right(di_dj):
            if di_dj == (-1, 0):
                return (0, 1)
            elif di_dj == (0, 1):
                return (1, 0)
            elif di_dj == (1, 0):
                return (0, -1)
            else:
                return (-1, 0)
        
        current_loc = start_loc
        di_dj = (-1, 0)
        while current_loc[0] >= 0 and current_loc[0] < len(grid) and current_loc[1] >= 0 and current_loc[1] < len(grid[0]):
            if not current_loc in visited:
                visited.add(current_loc)
            new_loc = (current_loc[0]+di_dj[0], current_loc[1]+di_dj[1])
            if (new_loc[0] >= 0 and new_loc[0] < len(grid) and new_loc[1] >= 0 and new_loc[1] < len(grid[0])) and grid[new_loc[0]][new_loc[1]] == "#":
                di_dj = turn_90_right(di_dj)
                current_loc = (current_loc[0]+di_dj[0], current_loc[1]+di_dj[1])
            else:
                current_loc = new_loc
        return visited
    
    def check_if_gets_stuck(self, fname: str, new_obstacle_loc: Tuple[int, int]) -> bool:
        grid, start_loc = solution.read_input(fname)
        grid[new_obstacle_loc[0]] = grid[new_obstacle_loc[0]][:new_obstacle_loc[1]]+"#"+grid[new_obstacle_loc[0]][new_obstacle_loc[1]+1:]
        di_dj = (-1, 0)
        visited = dict()

        def turn_90_right(di_dj):
            if di_dj == (-1, 0):
                return (0, 1)
            elif di_dj == (0, 1):
                return (1, 0)
            elif di_dj == (1, 0):
                return (0, -1)
            else:
                return (-1, 0)
        
        current_loc = start_loc
        while current_loc[0] >= 0 and current_loc[0] < len(grid) and current_loc[1] >= 0 and current_loc[1] < len(grid[0]):
            if not current_loc in visited:
                visited[current_loc] = {di_dj}
            else:
                if di_dj in visited[current_loc]:
                    return True
                visited[current_loc].add(di_dj)
            new_loc = (current_loc[0]+di_dj[0], current_loc[1]+di_dj[1])
            if (new_loc[0] >= 0 and new_loc[0] < len(grid) and new_loc[1] >= 0 and new_loc[1] < len(grid[0])) and grid[new_loc[0]][new_loc[1]] == "#":
                di_dj = turn_90_right(di_dj)
                current_loc = (current_loc[0]+di_dj[0], current_loc[1]+di_dj[1])
            else:
                current_loc = new_loc
        return False
    
    def check_if_gets_stuck_fast(self, fname: str, new_loc: Tuple[int, int]) -> bool:
        grid, start_loc = solution.read_input(fname)
        grid[new_loc[0]] = grid[new_loc[0]][:new_loc[1]]+"#"+grid[new_loc[0]][new_loc[1]+1:]
        di_dj = (-1, 0)
        visited = set()

        def turn_90_right(di_dj):
            if di_dj == (-1, 0):
                return (0, 1)
            elif di_dj == (0, 1):
                return (1, 0)
            elif di_dj == (1, 0):
                return (0, -1)
            else:
                return (-1, 0)
        
        current_loc = start_loc
        while True:
            if current_loc+di_dj in visited:
                return True
            visited.add(current_loc+di_dj)
            rr = current_loc[0]+di_dj[0]
            cc = current_loc[1]+di_dj[1]
            if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
                return False 
            elif grid[rr][cc] == "#":
                di_dj = turn_90_right(di_dj)
            else:
                current_loc = (rr, cc)
    
    def part02(self, fname: str):
        grid, _ = solution.read_input(fname)
        visited = solution.part01(fname)
        count = 0
        print(len(visited))
        for (i,j) in visited:
            if grid[i][j] not in ["#", "^"]:
                if self.check_if_gets_stuck_fast(fname, (i,j)):
                    count += 1
        return count

    def parse_test(self, fname: str):
        grid, _ = self.read_input(fname)
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "X":
                    visited.add((i,j))
        return visited
    
    def read_input(self, fname: str) -> Tuple[List[List[str]], Tuple[int, int]]:
        result = []
        start_loc = (0,0)
        with open(fname, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                stripped_line = line.strip()
                for j in range(len(stripped_line)):
                    if stripped_line[j] == '^':
                        start_loc = (i,j)
                result.append(stripped_line)
        return result, start_loc
    
    def test(self):
        visited_run = self.part01("sample.txt")
        visited_test = self.parse_test("test.txt")
        print("Run visited:", visited_run)
        print("Test visited:", visited_test)
        print("Missing from run:", visited_test - visited_run)
        print("Extra in run:", visited_run - visited_test)
        print(len(visited_run & visited_test) == len(visited_test))

if __name__ == "__main__":
    solution = Solution()
    #solution.test()
    #print(solution.read_input("sample.txt"))
    print(solution.part02("input.txt"))
