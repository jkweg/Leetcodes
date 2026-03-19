class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x* (-1)
            x = str(x)
            x = x[::-1]
            x = int(x)
            x = x*(-1)
            if x < -(2**31):
                return 0
            return x
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x > (2**31)-1:
                return 0
            return x