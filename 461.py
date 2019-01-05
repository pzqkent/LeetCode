class Solution(object):
    def hammingDistance(self, x, y):
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        if len(xb) > len(yb):
            len1 = len(xb)
            yb = '0' * (len(xb) - len(yb)) + yb
        else:
            len1 = len(yb)
            xb = '0' * (len(yb) - len(xb)) + xb
            
        counter = 0
        for i in range(len1):
            if xb[i] != yb[i]:
                counter += 1
        
        return counter
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        