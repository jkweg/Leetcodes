class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if min(nums) < k: return -1
        n = len(nums)
        wart = []
        for i in range(n):
            if nums[i] not in wart:
                wart.append(nums[i])
        x = len(wart)
        if k in wart:
            x -= 1
        return x