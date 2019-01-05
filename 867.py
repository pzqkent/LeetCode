class Solution(object):
    def transpose(self, A):
        result = []
        for i in range(len(A[0])):
            result.append([0] * len(A))
        # print(result)
        for i in range(len(A)):
            for j in range(len(A[i])):
                result[j][i] = A[i][j]
        return result
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        