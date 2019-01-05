class Solution:
    def twoSum(self, numbers, target):
        left,right = 0,len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
# class Solution(object):
#     def twoSum(self, numbers, target):
#         for i,j in enumerate(numbers):
#             if target - j in (numbers[:i] + numbers[i+1:]):
#                 return [i+1, (numbers[:i] + numbers[i+1:]) .index(target - j) + 2]
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, num in enumerate(numbers):
            if (target - num) in num_dict:
                return [num_dict[target - num], i + 1]
            num_dict[num] = i + 1
