from typing import List, Tuple
from functools import reduce

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
    
    def part02_brute_force(self, fname) -> int:
        line = self.read_input(fname)
        #print(len(line))
        full_output = []
        file_block_locs = []
        empty_block_locs = []
        for i, block_size in enumerate(line):
            #print(i, block_size)
            if i % 2 == 0:
                #full_output.extend([i//2 for _ in range(block_size)])
                if block_size > 0:
                    start_interval = len(full_output)
                    end_interval = start_interval+block_size-1
                    file_block_locs.append((i//2, (end_interval, start_interval)))
                for _ in range(block_size):
                    full_output.append(i//2)
            else:
                #full_output.extend(['.' for _ in range(block_size)])
                if block_size > 0:
                    start_interval = len(full_output)
                    end_interval = start_interval+block_size-1
                    empty_block_locs.append((start_interval, end_interval))
                for _ in range(block_size):
                    full_output.append('.')
            #print(full_output, len(full_output))
        
        #print(file_block_locs[::-1])
        #print(empty_block_locs)

        #print("Swapping")
        
        for file_id, (file_end, file_start) in file_block_locs[::-1]:
            #print(f"file_id: {file_id}, ({file_end}, {file_start})")
            for j, (empty_start, empty_end) in enumerate(empty_block_locs):
                #print(f"index: {j}, ({empty_start}, {empty_end})")
                if empty_end < file_start:
                    if empty_end-empty_start > file_end-file_start:
                        for x, y in zip(range(file_end, file_start-1, -1), range(empty_start, empty_start+(file_end-file_start+1)+1)):
                            #print(y, x)
                            full_output[y] = full_output[x]
                            full_output[x] = "."
                        empty_block_locs[j] = (empty_end-(file_end-file_start)+1, empty_end)
                        break
                    elif empty_end-empty_start == file_end-file_start:
                        for x, y in zip(range(file_end, file_start-1, -1), range(empty_start, empty_start+(file_end-file_start+1)+1)):
                            #print(y, x)
                            full_output[y] = full_output[x]
                            full_output[x] = "."
                        empty_block_locs.pop(j)
                        break
            #print(full_output)
            #print(file_block_locs)
            #print(empty_block_locs)
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

if __name__ == "__main__":
    solution = Solution()
    #print(solution.read_input("sample.txt"))
    print(solution.part02("sample.txt"))
