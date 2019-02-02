class Solution:
    def isHappy(self, n):
        n1 = n
        n = str(n)
        n = list(n)
        n = list(map(int,n))
        
        def pow1(x):
            return x**2
        n = list(map(pow1,n))
        sum1 = sum(n)
        print(sum1)
        if sum1 == 1:
            return True
        elif sum1 == 4:
            return False
        else:
            return self.isHappy(str(sum1))

        
        """
        :type n: int
        :rtype: bool
        """




class Solution:
    def isHappy(self,n):
        def sum_n(n):
            total = 0
            while n > 0:
                total += (n%10)**2
                n = n // 10
            return total
        total = sum_n(n)
        have_seen = []
        while total not in have_seen:
            if total == 1:
                return True
            else:
                have_seen.append(total)
                total = sum_n(total)
        return False