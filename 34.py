class Solution:
    def searchRange(self, nums, target):
        nums1 = list(map(lambda x: str(x), nums))
        # print(nums1)
        # print(target)
        try:
            return [nums1.index(str(target)),len(nums1) - nums1[::-1].index(str(target)) - 1]
        except:
            return [-1,-1]
        

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        