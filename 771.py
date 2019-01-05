class Solution(object):
    def numJewelsInStones(self, J, S):
        i = 0
        for letter in S:
            if letter in J:
                i += 1
        return i
                
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        