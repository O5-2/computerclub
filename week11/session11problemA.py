# Leetcode problem: Valid Anagram (242)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dS = defaultdict(int)
        dT = defaultdict(int)
        for i in s:
            dS[i] += 1
        for i in t:
            dT[i] += 1
        return dS == dT

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
