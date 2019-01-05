class Solution:
    def productExceptSelf(self, nums):
        result = [0] * len(nums)
        # print(result)
        multy = 1
        if 0 in nums:
            index1 = nums.index(0)
            # nums.pop(index1)
            nums[index1] = 1
            if 0 in nums:
                return [0] * (len(nums))
            else:
                for i in range(len(nums)):
                    multy *= nums[i]
                result[index1] = multy
                return result
                # print(result)
        # multy = 1
        for word in nums:
            multy *= word
        result = [multy] * len(nums)
        for i in range(len(nums)):
            result[i] = result[i] // nums[i]
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        