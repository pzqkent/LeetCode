# import string
class Solution:
    def isPalindrome(self, s):
        s1 = filter(str.isalnum, s)
        s1 = ''.join(list(s1))
        s1 = s1.lower()
        
        print(s1)
        return s1 == s1[::-1]
        
        """
        :type s: str
        :rtype: bool
        """
        