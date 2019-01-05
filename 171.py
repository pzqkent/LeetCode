class Solution:
    def titleToNumber(self, s):
        result = 0
        for i in range(1,len(s)+1):
            result = result + (ord(s[-i]) -65 + 1) * 26 ** (i - 1)
        return result
        """
        :type s: str
        :rtype: int