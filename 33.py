class Solution:
    def search(self, nums, target):
        try:
            return nums.index(target)
        except:
            return -1
        # return sorted(nums).index(target)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        