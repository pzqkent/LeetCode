class Solution:
    def wordPattern(self, pattern, str):
        list1 = str.split(' ')
        list2 = list(pattern)
        return list(map(list1.index,list1)) == list(map(list2.index,list2))
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """