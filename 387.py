from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        c1 = Counter(s)
        tuple1 = list(c1.items())
        print(tuple1)
        tuple1 = sorted(tuple1,key = lambda x: (x[1],tuple1))
        if tuple1[0][1] == 1:
            return s.index(tuple1[0][0])
        else:
            return -1
        """
        :type s: str
        :rtype: int
        """
        