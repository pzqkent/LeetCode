class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        elif len(nums) == 1:
            return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0],nums[1])
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        print(dp)
        return dp[-1]


思路二
上面的代码使用的空间是冗余的，因为每次循环只会用到前两个数据。所以代码可以降低空间复杂度到O(1)。

代码

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = last = 0
        for i in nums:
            last, now = now, max(i+last, now)
        return now
--------------------- 
