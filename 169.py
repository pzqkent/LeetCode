class Solution(object):
    def majorityElement(self, nums):
        len1 = len(nums) // 2 
        
        return sorted(nums)[len1]
        """
        :type nums: List[int]
        :rtype: int
        """
        