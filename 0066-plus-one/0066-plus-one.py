class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n -1
        while i >= 0:
            if digits[i]!=9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            i-= 1
        digits.append(0)
        digits[0] = 1
        return digits