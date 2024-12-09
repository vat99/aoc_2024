from typing import List, Tuple
from itertools import combinations


class Solution:
    def get_antinode(self, pair, H, W) -> List[tuple[int, int]]:
        loc1, loc2 = pair
        diff = (loc1[0]-loc2[0], loc1[1]-loc2[1])
        new_loc1 = (loc1[0]+diff[0], loc1[1]+diff[1])
        new_loc2 = (loc2[0]-diff[0], loc2[1]-diff[1])
        result = []
        if 0 <= new_loc1[0] < H and 0 <= new_loc1[1] < W:
            result.append(new_loc1)
        if 0 <= new_loc2[0] < H and 0 <= new_loc2[1] < W:
            result.append(new_loc2)
        return result
    
    def get_line(self, pair, H, W) -> List[tuple[int, int]]:
        loc1, loc2 = pair
        diff = (loc2[0]-loc1[0], loc2[1]-loc1[1])
        new_loc1 = (loc1[0]-diff[0], loc1[1]-diff[1])
        result = [loc1, loc2]
        while 0 <= new_loc1[0] < H and 0 <= new_loc1[1] < W:
            result.append(new_loc1)
            new_loc1 = (new_loc1[0]-diff[0], new_loc1[1]-diff[1])
        new_loc2 = (loc2[0]+diff[0], loc2[1]+diff[1])
        while 0 <= new_loc2[0] < H and 0 <= new_loc2[1] < W:
            result.append(new_loc2)
            new_loc2 = (new_loc2[0]+diff[0], new_loc2[1]+diff[1])
        return result
    
    def part01(self, fname):
        groups, H, W = self.read_input(fname)
        points = set()
        for group_key, group_list in groups.items():
            for pair in combinations(group_list, 2):
                antinodes = self.get_antinode(pair, H, W)
                for antinode in antinodes:
                    points.add(antinode)
        return len(points)
        
    def part02(self, fname):
        groups, H, W = self.read_input(fname)
        points = set()
        for group_key, group_list in groups.items():
            for pair in combinations(group_list, 2):
                #print(pair)
                antinodes = self.get_line(pair, H, W)
                for antinode in antinodes:
                    #print(antinode)
                    points.add(antinode)
                #print("*"*10)
        #print(points)
        return len(points)

    def read_input(self, fname: str) -> Tuple[dict, int, int]:
        result = dict()
        with open(fname, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                split_line = line.strip()
                for j, char in enumerate(split_line):
                    if char != ".":
                        if char in result:
                            result[char].append((i,j))
                        else:
                            result[char] = [(i,j)]
        return result, len(lines), len(line.strip())


if __name__ == "__main__":
    solution = Solution()
    #print(solution.read_input("sample.txt"))
    #print(solution.get_antinode(((3, 4),(5, 5)))) # (1,3), (7,6)
    #print(solution.part01("input.txt"))
    #print(solution.get_line(((0, 0), (2, 1)), 12, 12))
    print(solution.part02("input.txt"))
