from collections import Counter
class Solution:
    def findTheDifference(self, s, t):
        c1 = Counter(s)
        c2 = Counter(t)
        difference = c2 - c1
        difference = list(difference.elements())
        
        return difference[0]
        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        