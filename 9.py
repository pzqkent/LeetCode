class Solution(object):
    def isPalindrome(self, x):
        result = False
        if x < 0:
            result = False
        else:
            listx = list(str(x))
            reverse_x = list(reversed(listx))
            # print(listx, reverse_x)
            if listx == reverse_x:
                result = True
        return result
        """
        :type x: int
        :rtype: bool
        """
        