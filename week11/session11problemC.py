# Leetcode problem: Valid Parentheses (20)

class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        mapping = {'(': 1, ')': 1, '{': 2, '}': 2, '[': 3, ']': 3}
        for i in s:
            if i in "({[":
                q.append(mapping[i])
            else:
                if (len(q) == 0) or (q.pop() != mapping[i]):
                    return False
        return len(q) == 0

s = Solution()
print(s.isValid('()'))
print(s.isValid('()[]{}'))
print(s.isValid('(]'))
print(s.isValid('([)]'))
print(s.isValid('{[]}'))
