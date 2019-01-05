class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        cursum = maxsum = nums[0]
        for num in nums[1:]:
            cursum = max(num, cursum + num)
            maxsum = max(maxsum,cursum)
            
        return maxsum

        """
        :type nums: List[int]
        :rtype: int
        """