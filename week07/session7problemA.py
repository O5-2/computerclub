# Leetcode problem: Backspace String Compare (844)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        send = len(S)-1
        spound = 0
        tend = len(T)-1
        tpound = 0
        while (send >= 0) or (tend >= 0):
            if (send >= 0) and (S[send] == "#"):
                spound += 1
                send -= 1
            elif (tend >= 0) and (T[tend] == "#"):
                tpound += 1
                tend -= 1
            elif spound != 0:
                spound -= 1
                send -= 1
            elif tpound != 0:
                tpound -= 1
                tend -= 1
            elif (spound == 0) and (tpound == 0):
                if (S[send] != T[tend]) or ((send >= 0) ^ (tend >= 0)):
                    return False
                send -= 1
                tend -= 1
        return True

s = Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("ab##", "c#d#"))
print(s.backspaceCompare("a##c", "#a#c"))
print(s.backspaceCompare("a#c", "b"))
