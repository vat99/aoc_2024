from typing import List, Tuple


class Solution:
    def part01(self, fname: str) -> int:
        grid = self.read_input(fname)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] != 'X': 
                    continue
                else:
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            m_loc = (r + 1 * dr, c + 1 * dc)
                            a_loc = (r + 2 * dr, c + 2 * dc)
                            s_loc = (r + 3 * dr, c + 3 * dc)
                            in_bounds = lambda x, y: 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])
                            if in_bounds(*m_loc) and grid[m_loc[0]][m_loc[1]] == 'M' and in_bounds(*a_loc) and grid[a_loc[0]][a_loc[1]] == 'A' and in_bounds(*s_loc) and grid[s_loc[0]][s_loc[1]] == 'S':
                                count += 1
        return count
    
    def part02(self, fname: str) -> int:
        grid = self.read_input(fname)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] != 'A': 
                    continue
                else:
                    in_bounds = lambda x, y: 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])
                    if (
                        (
                            in_bounds(r-1, c-1) and grid[r-1][c-1] == 'M' and in_bounds(r+1, c-1) and grid[r+1][c-1] == 'M' and in_bounds(r-1, c+1) and grid[r-1][c+1] == 'S' and in_bounds(r+1, c+1) and grid[r+1][c+1] == 'S'
                        ) or
                        (
                            in_bounds(r-1, c-1) and grid[r-1][c-1] == 'M' and in_bounds(r+1, c-1) and grid[r+1][c-1] == 'S' and in_bounds(r-1, c+1) and grid[r-1][c+1] == 'M' and in_bounds(r+1, c+1) and grid[r+1][c+1] == 'S'
                        ) or
                        (
                            in_bounds(r-1, c-1) and grid[r-1][c-1] == 'S' and in_bounds(r+1, c-1) and grid[r+1][c-1] == 'S' and in_bounds(r-1, c+1) and grid[r-1][c+1] == 'M' and in_bounds(r+1, c+1) and grid[r+1][c+1] == 'M'
                        ) or
                        (
                            in_bounds(r-1, c-1) and grid[r-1][c-1] == 'S' and in_bounds(r+1, c-1) and grid[r+1][c-1] == 'M' and in_bounds(r-1, c+1) and grid[r-1][c+1] == 'S' and in_bounds(r+1, c+1) and grid[r+1][c+1] == 'M'
                        )
                    ):
                        count += 1
        return count

    def read_input(self, fname: str) -> List[List[str]]:
        result = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                result.append([x for x in line.strip()])
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input`.txt"))
