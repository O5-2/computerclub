# Leetcode problem: Perfect Squares (279)

class Solution:
    global required
    required = [0, 1, 2, 3]
    
    def numSquares(self, n: int) -> int:
        from math import sqrt
        from math import ceil
        global required
        specCeil = lambda n: int(n+1) if (n % 1 == 0) else ceil(n)
        if n < len(required):
            return required[n]
        for i in range(len(required), n+1):
            nums = [1+required[i-(j**2)] for j in range(1, min(len(required), specCeil(sqrt(i))))]
            required.append(min(nums))
        return required[n]

s = Solution()
print(s.numSquares(12))
print(s.numSquares(13))
print(s.numSquares(103))
print(s.numSquares(1004))
print(s.numSquares(10005))
print(s.numSquares(100006))

# Miniscule time for the low four digits.
# Half a second or so for the low five digits.
# Fifteen, twenty seconds for the low six digits.
# Is it good enough? Let's find out.
# I have made it a true global variable. Hopefully it doesn't backfire.
# It didn't.
