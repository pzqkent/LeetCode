class Solution:
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            n = n // 5
            result += n
        return result
        """
        :type n: int
        :rtype: int
        """
如果n=135:
135 // 5 = 27
135 // 25 = 5
135 // 125 = 1
result = 27+5+1=33

或者
135 // 5 = 27
27 // 5 = 5
5 // 5 = 1
result = 27+5+1=33

# 使用递归：
# class Solution(object):
#     def trailingZeros(self,n):
#         return 0 if n==0 else n // 5 + self.trailingZeros(n // 5)