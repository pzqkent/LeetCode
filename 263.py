class Solution:
    def isUgly(self, num):
        if num == 1:
            return True
        while num >=2 and num % 2 == 0:
            num = num // 2
        while num >= 3 and num % 3 == 0:
            num = num // 3
        while num >= 5 and num % 5 == 0:
            num = num // 5
        return num == 1
        """
        :type num: int
        :rtype: bool
        """


class Solution:
    def isUgly(self, num):
        if num == 0:
            return False
        while num % 2 == 0:
            num = num / 2
        while num % 3 == 0:
            num = num / 3
        while num % 5 == 0:
            num = num / 5
        return num == 1
        """
        :type num: int
        :rtype: bool
        """