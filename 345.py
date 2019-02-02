class Solution:
    def reverseVowels(self, s):
        index = []
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        slice1 = []
        list1 = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
                slice1.append(s[i])
        for j in range(1,len(index)+1):
            # list1[index[j-1]] = slice1[-j]
            list1[index[j-1]] = slice1.pop()
        return ''.join(list1)
        
                
            

        
        
        """
        :type s: str
        :rtype: str
        """
        