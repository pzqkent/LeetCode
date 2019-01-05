class Solution:
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        # find the shortest word in strs:
#         len1 = len(strs[0])
#         for i in range(len(strs)):
#             len1 = min(len1, len(strs[i]))
            
            

        result = ''
        for i in range(len(strs[0])):
            counter = 0
            for j in range(1,len(strs)):
                if i >= len(strs[j]):
                    break
                elif strs[j][i] == strs[0][i]:
                    counter += 1
                else:
                    break
            if counter == len(strs) - 1:
                # counter = 0
                if len(result) == i:
                    result += strs[0][i]
                else:
                    break
            else:
                break
        
        return result
                
                
                
                

        """
        :type strs: List[str]
        :rtype: str
        """
        