class Solution:
    def sortColors(self, nums):
        a,b,c = nums.count(0),nums.count(1),nums.count(2)
        nums[:] = [0 for i in range(a)] + [1 for j in range(b)] + [2 for k in range(c)]

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
class Solution:
    def sortColors(self, nums):
        # a,b,c = nums.count(0),nums.count(1),nums.count(2)
        # nums[:] = [0 for i in range(a)] + [1 for j in range(b)] + [2 for k in range(c)]
        
        a = collections.Counter(nums)
        nums[:] = list(a.elements())


# def sortColors(self, nums):
#     i = j = 0
#     for k in xrange(len(nums)):
#         v = nums[k]
#         nums[k] = 2
#         if v < 2:
#             nums[j] = 1
#             j += 1
#         if v == 0:
#             nums[i] = 0
#             i += 1

# # 86 / 86 test cases passed.
# # Status: Accepted
# # Runtime: 44 ms
# # 84.03%