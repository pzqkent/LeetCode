# class Solution:
#     def containsDuplicate(self, nums):
#         print(list(set(nums)))
#         return sorted(nums) != sorted(list(set(nums)))
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
class Solution:
    def containsDuplicate(self,nums):
        return len(nums) != len(set(nums))