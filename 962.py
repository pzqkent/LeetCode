# class Solution:

#         ans = 0
#         m = float('inf')
#         print(sorted(list(range(len(A))),key = A.__getitem__))
#         for i in sorted(list(range(len(A))), key = A.__getitem__):
#             ans = max(ans, i - m)
#             m = min(m,i)
#         return ans
        

                  
#         """
#         :type A: List[int]
#         :rtype: int
#         """
class Solution:
    def maxWidthRamp(self,A):
        B = sorted(list(range(len(A))),key = A.__getitem__)
        ans = 0
        min_element = B[0]
        for i in range(len(B)):
            if B[i] - min_element > ans:
                   ans = B[i] - min_element
            if B[i] < min_element:
                   min_element = B[i]
        return ans