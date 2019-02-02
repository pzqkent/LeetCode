class Solution:
    def isPerfectSquare(self, num):
        return num ** 0.5 == num // num ** 0.5
        """
        :type num: int
        :rtype: bool
        """