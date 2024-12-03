from typing import List, Tuple
import re
from functools import reduce


class Solution:
    def part01(self, fname: str) -> int:
        line = self.read_input(fname)
        matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
        return sum(
            map(
                lambda match: reduce(
                    lambda acc, el: acc * int(el), match[4:-1].split(","), 1
                ),
                matches,
            )
        )

    def part02(self, fname: str) -> int:
        line = self.read_input(fname)
        line = "do()" + line + "don't()"
        initial_matches = re.findall("do\(\)[\s\S]*?don't\(\)", line)
        result = 0
        for initial_match in initial_matches:
            matches = re.findall("mul\(\d{1,3},\d{1,3}\)", initial_match)
            result += sum(
                map(
                    lambda match: reduce(
                        lambda acc, el: acc * int(el), match[4:-1].split(","), 1
                    ),
                    matches,
                )
            )
        return result

    def read_input(self, fname: str) -> str:
        result = ""
        with open(fname, "r") as f:
            lines = f.readlines()
            for line in lines:
                result += line.strip()
        return result


if __name__ == "__main__":
    solution = Solution()
    # print(solution.part01("sample.txt")) 161
    print(solution.part02("input.txt"))
