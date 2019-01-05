class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        new_list = [[0] * c for i in range(r)]
        # print new_list
        new_list1 = []
        for i in range(len(nums)):
            new_list1 = new_list1 + nums[i]
        # print new_list1
        for i in range(r):
            # print(r,c)
            new_list[i] = new_list1[(0 + i * c):(c + i * c)]
        return new_list
                
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        