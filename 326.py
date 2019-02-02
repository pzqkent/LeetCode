class Solution:
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        if n < 1:
            return False
        while n % 3 == 0:
            
            if n / 3 == 1:
                return True

            else:
                n = n / 3
        return False
            
        """
        :type n: int
        :rtype: bool
        """