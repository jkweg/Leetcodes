from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        seen = set()

        for num in nums:
            if not num in seen:
                seen.add(num)
            else:
                return True
            
        return False