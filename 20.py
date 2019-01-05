class Solution:
    def isValid(self, s):
        myDict = {"(": ")", "[": "]", "{": "}"}
        myList = list(s)
        resultList = []

        for i in myList:
            if i in myDict.keys():
                resultList.append(i)
            else:
                if resultList == []:
                    return(False)
                elif myDict[resultList[-1]] == i:
                    resultList.pop()
                else:
                    return(False)

        if resultList == []:
            return(True)
        else:
            return(False)
# 很有新意的算法
#         # list1 = ['(',')','{','}','[',']']
#         # for i in range(len(s) // 2):
#         #     mirrorindex = len(s) - 1 - i
#         #     counter = 0
#         #     if s[i] == '(':
#         #         if s[mirrorindex] == ')':
#         #             counter += 1
#         #     elif s[i] == '{':
#         #         if s[mirrorindex] == '}':
#         #             counter += 1
#         #     elif s[i] == '[':
#         #         if s[mirrorindex] == ']':
#         #             counter += 1
#         #     else:
#         #         return False
#         #     if counter == len(s) // 2:
#         #         return True
#         if len(s) % 2 != 0:
#             return False
#         counter = 0
        
#         len1 = len(s)
#         # index1 = s.index('(')
#         # index2 = s.index('[')
#         # index3 = s.index('{')
        
#         if '(' in s:
#             index1 = s.index('(')
#             if index1 < len1 // 2:
#                 if s[index1 + 1] == ')' or s[len1-1-index1] == ')':
#                     counter +=1
#             elif index1 == len1 - 1:
#                 pass
#             else:
#                 if s[index1 + 1] == ')':
#                     counter +=1
#             # a = s.index('(')
            
#         print(counter)     

#         if '[' in s:
#             index2 = s.index('[')
#             # b = s.index('[')
#             if index2 < len1 // 2:
#                 if s[index2 + 1] == ']' or s[len1-1-index2] == ']':
#                     counter +=1
#             elif index2 == len1 - 1:
#                 pass
#             else:
#                 if s[index2 + 1] == ']':
#                     counter +=1
#         print(counter)    
        
#         if '{' in s:
#             index3 = s.index('{')
#             print(index3, len1)
            
#             # c = s.index('{')
#             if index3 < len1 // 2:
#                 if s[index3 + 1] == '}' or s[len1-1-index3] == '}':
#                     counter +=1
#             elif index3 == len1 - 1:
#                 pass
#             else:
#                 if s[index3 + 1] == '}':
#                     counter +=1
         
#         print(counter)   
            

#         if counter ==len(s) // 2:
#             return True
#         else:
#             return False
        
            
            
        
        """
        :type s: str
        :rtype: bool
        """
        