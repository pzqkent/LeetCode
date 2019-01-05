class Solution(object):
    def arrayPairSum(self, nums):
        total = 0
        nums.sort()
        numgroup = len(nums) / 2
        j = 0
        for i in range(numgroup):
             
            total += nums[j]
            j = j + 2

        return total

        """
        :type nums: List[int]
        :rtype: int
        """
        