from typing import List, Tuple
from collections import deque
from functools import reduce

class Solution:
    def read_input(self, fname) -> List[List[str]]:
        grid = []
        with open(fname, 'r') as f:
            for line in f.readlines():
                grid.append(line.strip())
        return grid
    
    def bfs(self, start_loc, visited, grid):
        group = []
        queue = deque([start_loc])
        visited.add(start_loc)
        while queue:
            i,j = queue.popleft()
            edges = 0
            for dx, dy in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = dx + i, dy + j
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[i][j] == grid[nx][ny] and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                # check if on edge or borders another value
                if nx < 0 or nx == len(grid) or ny < 0 or ny == len(grid[0]) or grid[nx][ny] != grid[i][j]:
                    edges += 1
            group.append(edges)
        return len(group)*sum(group)
    
    def bfs_pt2(self, start_loc, visited, grid):
        group = []
        queue = deque([start_loc])
        visited.add(start_loc)
        dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
        def is_good(x, y, nx, ny):
            return 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[i][j] == grid[nx][ny]
        corners = 0
        while queue:
            i,j = queue.popleft()
            for dx, dy in dirs:
                nx, ny = dx + i, dy + j
                if is_good(i, j, nx, ny) and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
            for k in range(len(dirs)):
                di_1, dj_1 = dirs[k]
                di_2, dj_2 = dirs[(k+1)%len(dirs)]
                if not is_good(i, j, i+di_1, j+dj_1) and not is_good(i, j, i+di_2, j+dj_2):
                    corners += 1
                elif is_good(i, j, i+di_1, j+dj_1) and is_good(i, j, i+di_2, j+dj_2) and not is_good(i,j, i+di_1+di_2, j+dj_1+dj_2):
                    corners += 1

            group.append((i,j))
        return len(group) * corners

    
    def part01(self, fname) -> int:
        grid = self.read_input(fname)
        visited = set()
        total_price = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    total_price += self.bfs((i,j), visited, grid)
        return total_price
    
    def part02(self, fname) -> int:
        grid = self.read_input(fname)
        visited = set()
        total_price = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    total_price += self.bfs_pt2((i,j), visited, grid)
        return total_price
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input.txt"))