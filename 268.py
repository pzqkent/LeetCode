# class Solution:
#     def missingNumber(self, nums):
#         entire = [i for i in range(max(nums)+1)]
        
#         if sorted(nums) == entire:
#             return max(nums) + 1
#         else:
#             return [i for i in entire if i not in nums][0]

#         """
#         :type nums: List[int]
#         :rtype: int
#         """

class Solution:
    def missingNumber(self, nums):

        entire = list(range(max(nums)+1))
        # print(set(nums))
        # difference = set(entire) - set(nums)
        difference = list(set(entire) - set(nums))
        # print(difference)
        if len(difference) == 0:
            return max(nums) + 1
        else:
            return difference[0]