class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        maxi = cnt = 1
        x = 0

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                cnt += 1
            else:
                if cnt > maxi:
                    maxi = cnt
                    x = nums[i]
                cnt = 1
        if cnt > maxi:
            x = nums[-1]
        return x

        