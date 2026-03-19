class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 7:
            return True
        elif n < 10:
            return False
        else:
            res = 0
            while n >0:
                x = n%10
                res += x*x
                n = n//10
            return self.isHappy(res)
        