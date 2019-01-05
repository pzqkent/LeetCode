class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        elif len(nums) <= 2:
            return max(nums[0],nums[-1])

        return max(self.robber(nums[1:]),self.robber(nums[:-1]))
        # a = self.robber(nums)
        # return a
    
    def robber(self,nums1):
        

        money = [0]*len(nums1)
        money[0], money[1] = nums1[0], max(nums1[0], nums1[1])
        for i in range(2, len(nums1)):
            money[i] = max(nums1[i] + money[i-2], money[i-1])
        
            
#         if nums[0] > nums[1]:
#             money[-1] = money[-2]
        print(money)
        return money[len(nums1)-1]
关键就是最后那一个房间N和第一个房间相连了，可以这么进行转化：

考虑抢劫了第0个房间，那么问题就是求抢劫第0~N-1个房间的最大数。

考虑不抢劫第0个房间，那么问题就是求抢劫第1~N个房间的最大数。

上面转化后的两个问题就是House Robber I中的问题。再求上面两个解的最大值，就是本题的解。
