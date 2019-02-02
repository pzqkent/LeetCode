class Solution:
    def licenseKeyFormatting(self, S, K):
        # s1 = filter(str.isalnum,S)
        # s1 = ''.join(list(s1))
        # s1 = s1.upper()
        # s1 = list(s1)
        s1 = list((''.join(S.split('-'))).upper())
        j = K
        for i in range((len(s1) - 1) // K):
            s1.insert(-j,'-')
            j = j + K + 1
        s1 = ''.join(s1)

        return s1
        
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        