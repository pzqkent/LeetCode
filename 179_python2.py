class Solution(object):
    def largestNumber(self, nums):
        nums.sort(cmp = lambda a,b: int(str(b)+str(a)) - int(str(a) + str(b)))
        # a = ''.join(nums)
        # print(nums)
        # a = ''.join(map(str,nums)).lstrip('0') or '0'
        # a = str(int(a))
        return ''.join(map(str,nums)).lstrip('0') or '0'
        """
        思路：对于数组中的任意两个数a,b，利用sort()函数的cmp参数，如果int(str(b)+str(a)) > int(str(a)+str(b)), 则调换a和b的位置
        否则保持位置不变
        :type nums: List[int]
        :rtype: str
        """
        