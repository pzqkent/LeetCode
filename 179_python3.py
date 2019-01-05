# class Solution:
#     def largestNumber(self, nums):
#         from functools import cmp_to_key
#         # nums.sort(key = cmp_to_key(lambda a,b: int(str(b)+str(a)) - int(str(a) + str(b))))
#         # nums.sort(key = lambda a,b: int(str(b)+str(a)) - int(str(a) + str(b)))
        
#         return ''.join(map(str,sorted(nums,key = cmp_to_key(lambda a,b: int(str(b)+str(a)) - int(str(a) + str(b)))))).lstrip('0') or '0'
        
#         """
#         :type nums: List[int]
#         :rtype: str
#         """
        
        
class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        字符串也好，列表也好，都是可迭代对象。
		先比较两个对象的第0个元素，大小关系即为对象的大小关系，如果相等则继续比较后续元素，先终止迭代的认为是小的。
        """
        return str(int(''.join(sorted(map(str, nums), key = lambda _: _ * 9, reverse = True))))