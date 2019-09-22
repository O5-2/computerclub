# Leetcode problem: Reverse Vowels of a String (345)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a","e","i","o","u","A","E","I","O","U"])
        low = 0
        high = len(s) - 1
        ans = list(s)
        while high > low:
            if ans[low] not in vowels:
                low += 1
            if ans[high] not in vowels:
                high -= 1
            if ans[low] in vowels and ans[high] in vowels:
                store = ans[low]
                ans[low] = ans[high]
                ans[high] = store
                low += 1
                high -= 1
        return "".join(ans)

s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
