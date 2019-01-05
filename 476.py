class Solution(object):
    def findComplement(self, num):
        bnum = bin(num)[2:]
        result = ''
        for i in range(len(bnum)):
            result = result + str(int(bnum[i]) ^ 1)
            
        # print int(result,2)
        return int(result,2)
        
        
        
        """
        :type num: int
        :rtype: int
        """
        