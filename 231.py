class Solution:
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        while n>0:
            a = n / 2
            if a == 1:
                return True
            elif a % 2 == 0:
                n = n // 2
            else:
                return False
        return False
        """
        :type n: int
        :rtype: bool
        """