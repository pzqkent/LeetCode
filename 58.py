class Solution:
    def lengthOfLastWord(self, s):
        if list(s.split()) == []:
            return 0
        else:
            # return len(list(s.split(''))[-1]) if len(list(s.split(''))[-1]) != 0 else len(list(s.split(''))[-2])
            return len(list(s.split())[-1])
        """
        :type s: str
        :rtype: int
        """