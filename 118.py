class Solution:
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            result.append([1] * (i + 1))
        if numRows > 2:
            for j in range(2,numRows):
                for k in range(1,j):
                    result[j][k] = result[j-1][k-1] + result[j-1][k]
                    # print(j,k)
        
        return result
        

        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        