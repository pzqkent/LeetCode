class Solution:
    def plusOne(self, digits):

        result = ''
        result1 = []
        for i in range(len(digits)):
            result += str(digits[i])
        
        result = int(result) + 1
        [result1.append(int(i)) for i in str(result)]
        
        return result1
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        