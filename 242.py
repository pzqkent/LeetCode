from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        