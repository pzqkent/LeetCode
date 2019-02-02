
class Solution:
    def maximumGap(self, nums):
        
        if len(nums) < 2:
            return 0
        nums.sort()
        difference = 0
        for i in range(len(nums)-1):
            temp = nums[i+1] - nums[i]
            if temp > difference:
                difference = temp
                
                
        return difference
        """
        :type nums: List[int]
        :rtype: int
        """
        