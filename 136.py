class Solution(object):
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
#         A = list(set(nums))
        
#         for letter in nums:
#             if letter not in A:
#                 return A