# Leetcode problem: Open the Lock (752)

from typing import List

class Solution:
    def neighbors(self, combination: str) -> List[str]:
        a = str((int(combination[0])+1) % 10)+combination[1:]
        b = str((int(combination[0])-1) % 10)+combination[1:]
        c = combination[0]+str((int(combination[1])+1) % 10)+combination[2:]
        d = combination[0]+str((int(combination[1])-1) % 10)+combination[2:]
        e = combination[:2]+str((int(combination[2])+1) % 10)+combination[3]
        f = combination[:2]+str((int(combination[2])-1) % 10)+combination[3]
        g = combination[:3]+str((int(combination[3])+1) % 10)
        h = combination[:3]+str((int(combination[3])-1) % 10)
        return [a, b, c, d, e, f, g, h]
    
    def openLock(self, deadends: List[str], target: str) -> int:
        s = Solution()
        combinations = [("0000", 0)]
        values = set([0])
        if target == "0000":
            return -1*int(False ^ ("0000" in deadends))
        i = 0
        #minMoves = 10001
        while i < len(combinations):
            if combinations[i][0] not in deadends:
                for j in s.neighbors(combinations[i][0]):
                    if int(j) not in values:
                        combinations.append((j, combinations[i][1]+1))
                        values.add(int(j))
                    if j == target:
                        return combinations[i][1]+1
                        #minMoves = min(minMoves, combinations[i][1]+1)
            i += 1
        #if minMoves == 10001:
        #    minMoves = -1
        return -1

s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))
print(s.openLock(["8888"], "0009"))
print(s.openLock(["0001"], "0000"))
print(s.openLock(["0000"], "0000"))
print(s.openLock([], "5555"))
# This is kind of slow. Each trial takes about a quarter of a second. Does it really take that long to go through 10k possibilities?
# With, say, 100m operations per second, that's either quadratic time or really awful linear time.

# I just thought of something. Using BFS, it's guaranteed that the first solution will be the correct one.
# Alright, with that improvement we've gotten things up to ~40, 50 milliseconds for the early ones,
# but it's still a quarter of a second for 5555 and similar, things that take twenty moves or so.

# Well, it's correct according to Leetcode, but it takes 1.1 seconds (bottom fifth) and 16 megabytes of memory (bottom eighth).
# I should go over this with Dad.
