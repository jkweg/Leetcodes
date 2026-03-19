class Solution:
    def isPalindrome(self, x: int):
        x = str(x)
        return x == x[::-1]