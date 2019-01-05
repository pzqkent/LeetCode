class Solution(object):
    def removeElement(self, nums, val):
        # for i in range(0,len(nums)):
        #     if nums[i] == val:
        #         nums.remove(val)
        # return len(nums)
        index = [i for i,v in enumerate(nums) if v == val]
        [nums.remove(val) for i in range(len(index))]
        # print(len(index))
        # # [nums.pop(x) for x in index]
        return len(nums)

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        