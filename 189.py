class Solution:
    def rotate(self, nums, k):
        for i in range(k): nums.insert(0,nums.pop(-1))

        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """