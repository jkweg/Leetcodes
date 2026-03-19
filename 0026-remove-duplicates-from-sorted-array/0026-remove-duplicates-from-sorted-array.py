class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1 2 3 4 4 5 6 7 
        # 1 2 3 4 4
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j