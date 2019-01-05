class Solution(object):
    def hasAlternatingBits(self, n):

        # if len(n) == 1:
        #     return True
        n_bin = bin(n)[2:]
        return all(n_bin[i] != n_bin[i+1] for i in range(len(n_bin) - 1))

            
        """
        :type n: int
        :rtype: bool
        """
        