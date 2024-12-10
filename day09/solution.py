from typing import List, Tuple
from functools import reduce
from heapq import heappush, heappop

class Solution:
    def read_input(self, fname) -> List[int]:
        with open(fname, 'r') as f:
            return list(map(int, f.readline().strip()))
    
    def part01_brute_force(self, fname) -> int:
        line = self.read_input(fname)
        #print(len(line))
        full_output = []
        file_block_locs = []
        empty_block_locs = []
        for i, block_size in enumerate(line):
            if i % 2 == 0:
                #full_output.extend([i//2 for _ in range(block_size)])
                for _ in range(block_size):
                    full_output.append(i//2)
                    file_block_locs.append(len(full_output)-1)
            else:
                #full_output.extend(['.' for _ in range(block_size)])
                for _ in range(block_size):
                    full_output.append('.')
                    empty_block_locs.append(len(full_output)-1)
        #print(full_output)

        # for i in range(len(full_output)):
        #     if full_output[i] == '.':
        #         j = i+1
        #         while j < len(full_output) and full_output[j] == '.':
        #             j += 1
        #         if j < len(full_output):
        #             temp = full_output[i]
        #             full_output[i] = full_output[j]
        #             full_output[j] = temp
        # print(full_output)

        # i is first '.' index
        # j is last num index
        # swap i and j
        # increment i to next '.' index
        # decrement j to next num index
        # keep going until i meets j

        # assuming file_block_locs and empty_block_locs are non-empty
        #print(file_block_locs[::-1])
        #print(empty_block_locs)
        for empty_block_index, file_block_index in zip(empty_block_locs, file_block_locs[::-1]):
            if empty_block_index < file_block_index:
                full_output[empty_block_index] = full_output[file_block_index]
                full_output[file_block_index] = '.'
                #print(empty_block_index, file_block_index)
                #print(full_output)
            else:
                break
        #print(list(enumerate(full_output)))
        return reduce(lambda x, y: x + (y[0]*y[1]) if y[1] != '.' else x, enumerate(full_output), 0)

    def part02(self, fname) -> int:
        line = self.read_input(fname)
        #print(len(line))
        full_output = []
        file_block_locs = []
        empty_block_locs = []
        file_id = 0
        pos = 0
        for i, sz in enumerate(line):
            if i % 2 == 0:
                file_block_locs.append((pos, sz, file_id))
                for i in range(sz):
                    full_output.append(file_id)
                    pos += 1
                file_id += 1
            else:
                empty_block_locs.append((pos, sz))
                for i in range(sz):
                    full_output.append(".")
                    pos += 1
        
        for (pos, sz, file_id) in reversed(file_block_locs):
            for empty_i, (empty_pos, empty_sz) in enumerate(empty_block_locs):
                if empty_pos < pos and sz <= empty_sz:
                    for i in range(sz):
                        full_output[empty_pos+i] = file_id
                        full_output[pos+i] = "."
                    empty_block_locs[empty_i] = (empty_pos+sz, empty_sz-sz)
                    break
        return reduce(lambda x, y: x + (y[0]*y[1]) if y[1] != '.' else x, enumerate(full_output), 0)
    
    def part02_optimized(self, fname) -> int:
        line = self.read_input(fname)
        full_output = []
        file_blocks = []
        empty_blocks = [[] for _ in range(10)]
        pos = 0
        file_id = 0
        for i, sz in enumerate(line):
            if i % 2 == 0:
                file_blocks.append((pos, sz, file_id))
                for _ in range(sz):
                    full_output.append(file_id)
                    pos += 1
                file_id += 1
            else:
                heappush(empty_blocks[sz], pos)
                for _ in range(sz):
                    full_output.append('.')
                    pos += 1
        for pos, sz, file_id in reversed(file_blocks):
            for empty_sz in range(sz, len(empty_blocks)):
                if len(empty_blocks[empty_sz]) > 0 and pos > empty_blocks[empty_sz][0]:
                    leftmost_empty_interval = heappop(empty_blocks[empty_sz])
                    for i in range(sz):
                        full_output[leftmost_empty_interval+i] = file_id
                        full_output[pos+i] = '.'
                    heappush(empty_blocks[empty_sz-sz], leftmost_empty_interval+sz)
                    break

        return reduce(lambda x, y: x + (y[0]*y[1]) if y[1] != '.' else x, enumerate(full_output), 0)

if __name__ == "__main__":
    solution = Solution()
    #print(solution.read_input("sample.txt"))
    #print(solution.part02("test.txt"))
    print(solution.part02_optimized("test2.txt"))
