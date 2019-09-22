# Leetcode problem: Valid Palindrome (125)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()
        to_remove = [" ",":",";",".",",","~","`","!","@","#","$","%","^","&","*","(",")","_","-","+","=","<",">","{","[","}","]","?","'",'"']
        for i in to_remove:
            s = "".join(s.split(i))
        return s == s[::-1]

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
