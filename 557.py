class Solution(object):
    def reverseWords(self, s):
        s_split = s.split(' ')
        result = []
        # print(s_split)
        for item in s_split:
            item_reverse = ''.join(list(reversed(item)))
            result.append(item_reverse)
        return ' '.join(result)
            
        """
        :type s: str
        :rtype: str
        """
        