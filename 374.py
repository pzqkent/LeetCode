# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
# import random
# class Solution(object):
#     def guessNumber(self, n):
        
#         choice = random.randint(0,n)
        
#         feedback = guess(choice)
#         while feedback != 0:
            
#             if feedback == -1:
#                 choice = random.randint(0,choice)
#                 # feedback = guess(choice)
#             else:
#                 choice = random.randint(choice,n)
#                 # feedback = guess(choice)
#             feedback = guess(choice)
#         return choice 
#         """
#         :type n: int
#         :rtype: int
#         """
        
class Solution(object):
    def guessNumber(self,n):
        low,high = 1,n
        
        while low < high:
            mid = (low+high) // 2
            if guess(mid) == -1:
                high = mid
            elif guess(mid) == 1:
                low = mid + 1
            else:
                return mid
        return low
                