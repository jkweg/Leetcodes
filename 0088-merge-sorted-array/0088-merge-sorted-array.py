class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for j in range(len(nums2)):
            i = 0
            while i < m and nums2[j] > nums1[i]:
                i+=1
            for k in range(m,i,-1):
                nums1[k] = nums1[k-1]
            nums1[i] = nums2[j]
            m+=1
        