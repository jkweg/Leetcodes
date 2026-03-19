class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j] and (i * j)%k==0:
                    cnt += 1
        return cnt 
        