class Solution(object):
    def isToeplitzMatrix(self, matrix):

        b = []
        for k, l in enumerate(matrix):
            if 0 < k < len(matrix):
                if b != l[1:]:
                    return False
            b = l[:-1]
        return True  

        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        