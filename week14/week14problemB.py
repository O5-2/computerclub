# Leetcode problem: Prime Arrangements (1175)

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        p = 0
        c = 1
        num = 1
        if n == 1:
            return 1
        for i in range(2, n+1):
            if i in primes:
                p += 1
            else:
                c += 1
        for i in range(1, p+1):
            num *= i
            num = num % 1000000007
        for i in range(1, c+1):
            num *= i
            num = num % 1000000007
        return num

s = Solution()
print(s.numPrimeArrangements(5))
print(s.numPrimeArrangements(100))
print(s.numPrimeArrangements(1))
print(s.numPrimeArrangements(2))
print(s.numPrimeArrangements(3))
print(s.numPrimeArrangements(4))
# Answer = (number of primes up to and including n)! * (number of composites up to and including n)!

# Just a note: I couldn't access problem C because Leetcode made it premium-only.
