class Solution:
    def getSum(self, a, b):
        sum = a ^ b
        carry = (a & b) << 1
        sum += carry
        return sum
        """
        :type a: int
        :type b: int
        :rtype: int
        """