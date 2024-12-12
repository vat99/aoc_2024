from typing import List, Tuple
from collections import Counter
import math
from multiprocessing import Pool

class Solution:
    def read_input(self, fname) -> List[str]:
        with open(fname, 'r') as f:
            return f.readline().strip().split(" ")
        
    def part01(self, fname, steps) -> int:
        lst = self.read_input(fname)
        for _ in range(steps):
            new_lst = []
            for l in lst:
                if l == "0":
                    new_lst.append("1")
                elif len(l) % 2 == 0:
                    new_lst.append(l[:len(l)//2])
                    new_lst.append(str(int(l[len(l)//2:])))
                else:
                    new_lst.append(str(int(l)*2024))
            lst = new_lst
            #print(lst)
        return lst
        
    def process_chunk(self, lst, steps) -> int:
        for _ in range(steps):
            new_lst = []
            for l in lst:
                if l == "0":
                    new_lst.append("1")
                elif len(l) % 2 == 0:
                    new_lst.append(l[:len(l)//2])
                    new_lst.append(str(int(l[len(l)//2:])))
                else:
                    new_lst.append(str(int(l)*2024))
            lst = new_lst
        return len(lst)

    def part02(self, fname, steps) -> int:
        lst = self.read_input(fname)
        f = Counter(lst)
        print(f)
        for t in range(steps):
            nf = Counter()
            for x in f.keys():
                count = f[x]
                if x == "0":
                    nf["1"] += count
                elif len(x) % 2 == 0:
                    lx = x[:len(x)//2]
                    rx = str(int(x[len(x)//2:]))
                    nf[lx] += count
                    nf[rx] += count
                else:
                    nf[str(int(x)*2024)] += count
            f = nf

            print(t, sum(f.values()))
        return sum(f.values())
    
    def test(self):
        assert self.part01("sample2.txt", 6) == self.read_input("test2.txt")
        #print(self.part01("sample2.txt", 6))
        #print(self.read_input("test2.txt"))

if __name__ == "__main__":
    solution = Solution()
    #solution.test()
    print(solution.part02("input.txt", 75))