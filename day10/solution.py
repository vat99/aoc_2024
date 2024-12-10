from typing import List, Tuple
from collections import Counter

class Solution:
    def read_input(self, fname) -> Tuple[List[List[int]], List[Tuple[int, int]]]:
        grid = []
        trail_heads = []
        with open(fname, 'r') as f:
            for i, line in enumerate(f.readlines()):
                current_row = []
                for j, c in enumerate(line.strip()):
                    num = int(c) if c in '0123456789' else -1
                    if num == 0:
                        trail_heads.append((i,j))
                    current_row.append(num)
                grid.append(current_row)
        return grid, trail_heads
    
    def traverse(self, grid, trail_head):
        i,j = trail_head
        queue = [(i,j,0)]
        count = 0
        visited = set()
        while queue:
            i,j, prev_value = queue.pop(0)
            if (i,j) not in visited:
                visited.add((i,j))
                if grid[i][j] == 9:
                    count += 1
                else:
                    if 0 <= i-1 and grid[i-1][j] == prev_value+1: # up
                        queue.append((i-1, j, prev_value+1))
                    if i+1 < len(grid) and grid[i+1][j] == prev_value+1: # down
                        queue.append((i+1, j, prev_value+1))
                    if 0 <= j-1 and grid[i][j-1] == prev_value+1: # left
                        queue.append((i, j-1, prev_value+1))
                    if j+1 < len(grid[0]) and grid[i][j+1] == prev_value+1: # right
                        queue.append((i, j+1, prev_value+1))
        return count
    
    def part01(self, fname):
        grid, trail_heads = self.read_input(fname)
        count = 0
        for trail_head in trail_heads:
            print(trail_head)
            trail_head_score = self.traverse(grid, trail_head)
            print(trail_head_score)
            count += trail_head_score
        return count

    def traverse_count(self, grid, trail_head):
        i,j = trail_head
        queue = [(i,j)]
        counts = Counter()
        counts[(i,j)] = 1
        score = 0
        visited = set()
        visited.add((i,j))
        while queue:
            i,j = queue.pop(0)
            if grid[i][j] == 9:
                score += counts[(i,j)]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == grid[i][j] + 1 and (nx,ny) not in visited:
                    queue.append((nx,ny))
                    visited.add((nx,ny))
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == grid[i][j] + 1:
                    counts[(nx,ny)] += counts[(i,j)]
        return score
    
    def part02(self, fname):
        grid, trail_heads = self.read_input(fname)
        count = 0
        for trail_head in trail_heads:
            print(trail_head)
            trail_head_score = self.traverse_count(grid, trail_head)
            print(trail_head_score)
            count += trail_head_score
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("/home/vat23/coding/aoc_2024/day10/input.txt"))
