from typing import List, Tuple
from collections import defaultdict
from functools import cmp_to_key


class Solution:
    def part01(self, fname: str) -> int:
        blocks = solution.read_input(fname)
        before = defaultdict(set)
        for rule in blocks[0]:
            before[rule[1]].add(rule[0])

        def is_ordered(queue):
            for i in range(len(queue)):
                for j in range(i + 1, len(queue)):
                    if queue[j] in before[queue[i]]:
                        return False
            return True

        result = 0
        for queue in blocks[1]:
            if is_ordered(queue):
                print(queue)
                result += queue[(len(queue) // 2)]
        return result

    def part02(self, fname: str) -> int:
        blocks = solution.read_input(fname)
        before = defaultdict(set)
        for rule in blocks[0]:
            before[rule[1]].add(rule[0])

        def is_ordered(queue):
            for i in range(len(queue)):
                for j in range(i + 1, len(queue)):
                    if queue[j] in before[queue[i]]:
                        return False
            return True

        def compare(a, b):
            if a in before[b]:
                return 1
            elif b in before[a]:
                return -1
            return 0

        result = 0
        for queue in blocks[1]:
            if not is_ordered(queue):
                print(queue)
                queue.sort(key=cmp_to_key(compare))
                result += queue[(len(queue) // 2)]
        return result

    def read_input(self, fname: str) -> List[List[List[int]]]:
        result = []
        is_block_1 = True
        with open(fname, "r") as f:
            lines = f.readlines()
            block = []
            for line in lines:
                if line == "\n":
                    result.append(block)
                    block = []
                    is_block_1 = False
                else:
                    if is_block_1:
                        block.append(list(map(int, line.strip().split("|"))))
                    else:
                        block.append(list(map(int, line.strip().split(","))))
        result.append(block)
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.part02("input.txt"))
