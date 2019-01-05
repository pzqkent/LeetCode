class Solution:

# fast python solution
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
#         if n < 2:
#             return 0
#         result = 0
#         for i in range(2,n):
#             counter = 0
#             for j in range(2, int(i ** 0.5) + 1):
#                 if i % j != 0:
#                     counter += 1
#                 else:
#                     break
#             if counter == int(i ** 0.5) + 1 - 2:
#                 result += 1
        
#         return result
        """
        :type n: int
        :rtype: int
        """
        