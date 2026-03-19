class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        p = len(height)-1
        maxi = v = 0
        while l != p:
            v = (p - l)*min(height[l],height[p])
            if v > maxi:
                maxi = v
            if height[l] > height[p]:
                p -= 1
            else:
                l += 1
        return maxi

        