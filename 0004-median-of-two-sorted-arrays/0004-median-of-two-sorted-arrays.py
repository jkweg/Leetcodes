class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        l = len(nums)
        s = l//2
        if l % 2 == 0:
            return (nums[s-1] + nums[s])/2.0
        else:
            return nums[s]