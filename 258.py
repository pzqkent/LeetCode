class Solution:
    def addDigits(self, num):
        # total = 10
        def sum_num(x):
            total = 0
            while x >0:
                total = total + x % 10
                x = x // 10
            return total
        total = sum_num(num)
        
        while len(str(total)) != 1:
            total = sum_num(total)
        return total

            
            
        """
        :type num: int
        :rtype: int
        """p