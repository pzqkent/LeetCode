class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
#         maxnum,num,ss =0,0,''
#         for each in s:
#             print('each:',each)
#             print('ss:',ss)
#             if each in ss:
                
#                 print(ss.split(each))
                
                
#                 ss = ss.split(each)[-1]+each
#                 print('ss2',ss)
#                 num =len(ss)
#             else:
#                 num += 1
#                 ss += each
#                 if num>=maxnum:
#                     maxnum = num

#         return maxnum
    
    
        maxnum,num,ss = 0,0,''
        for letter in s:
            if letter in ss:
                ss = ss.split(letter)[-1]+letter
                num = len(ss)
            else:
                num+= 1
                ss += letter
                if num > maxnum:
                    maxnum = num
        return maxnum