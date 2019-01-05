class Solution(object):
    def isMonotonic(self, A):
        A1 = sorted(A)
        A2 = sorted(A,reverse = True)
        # A1.sort()
        # A2.reverse()
        # A2.reverse()
        # print A
        # print A1,A2
        if (A == A1) or (A == A2): 
            return True
        else:
            return False
        
        
 
        """
        :type A: List[int]
        :rtype: bool
        """
        