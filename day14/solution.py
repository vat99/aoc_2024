from typing import List, Tuple
from collections import deque
from functools import reduce
import re


class Solution:
    def read_input(self, fname):
        inputs = []
        with open(fname, "r") as f:
            for line in f.readlines():
                inputs.append(
                    tuple(
                        map(
                            lambda x: tuple(map(int, x[2:].split(","))),
                            line.strip().split(" "),
                        )
                    )
                )
        return inputs

    def part01_brute_force(self, fname, tsteps, width, height):
        inputs = self.read_input(fname)
        quads = [0, 0, 0, 0]
        print(len(inputs))
        for (px, py), (vx, vy) in inputs:
            nx, ny = (((px + vx * tsteps) % width), (py + vy * tsteps) % height)
            print(f"{px, py} -> {nx, ny}")
            if 0 <= nx < width // 2 and 0 <= ny < height // 2:
                quads[0] += 1
                print("quad 1")
            elif width // 2 < nx < width and 0 <= ny < height // 2:
                quads[1] += 1
                print("quad 2")
            elif 0 <= nx < width // 2 and height // 2 < ny < height:
                quads[2] += 1
                print("quad 3")
            elif width // 2 < nx < width and height // 2 < ny < height:
                quads[3] += 1
                print("quad 4")
            else:
                print("border")
        print(quads)
        return quads[0] * quads[1] * quads[2] * quads[3]


if __name__ == "__main__":
    solution = Solution()
    # print(solution.read_input("sample.txt"))
    # print(solution.read_input("sample.txt"))
    # print(solution.part01_brute_force("input.txt", 100, 101, 103))
    from re import findall

    data = open("input.txt").read()
    W, H = 101, 103

    robots = [[int(n) for n in findall(r"(-?\d+)", item)] for item in data.split("\n")]

    def simulate(t):
        return [((sx + t * vx) % W, (sy + t * vy) % H) for (sx, sy, vx, vy) in robots]

    from statistics import variance

    bx, bxvar, by, byvar = 0, 10 * 100, 0, 10 * 1000
    for t in range(max(W, H)):
        xs, ys = zip(*simulate(t))
        if (xvar := variance(xs)) < bxvar:
            bx, bxvar = t, xvar
        if (yvar := variance(ys)) < byvar:
            by, byvar = t, yvar
    print("Part 2:", bx + ((pow(W, -1, H) * (by - bx)) % H) * W)
