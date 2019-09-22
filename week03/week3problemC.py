# Leetcode problem: Find Smallest Letter Greater Than Target (852)

from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(0, len(letters)):
            if (target < letters[i]):
                return letters[i]
        return letters[0]
        
s = Solution()
print(s.nextGreatestLetter(["c", "f", "j"], "a"))
print(s.nextGreatestLetter(["c", "f", "j"], "c"))
print(s.nextGreatestLetter(["c", "f", "j"], "d"))
print(s.nextGreatestLetter(["c", "f", "j"], "g"))
print(s.nextGreatestLetter(["c", "f", "j"], "j"))
print(s.nextGreatestLetter(["c", "f", "j"], "k"))
