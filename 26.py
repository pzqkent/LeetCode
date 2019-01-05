class Solution(object):
    def removeDuplicates(self, nums):
        
        i = 0
        while i < len(nums) - 1:
            
        # for i in range(0,len(nums)-1):
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i = i + 1
                


                
        """
        :type nums: List[int]
        :rtype: int
        """
        