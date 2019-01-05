class Solution:
    def myAtoi(self, str):
        s = str.strip()
        try:
            result = ''
            for i in range(len(s)):
                if (s[i] in '+-' and i == 0) or '0' <= s[i] <= '9':
                    result += s[i]
                else:
                    break
            result = int(result)
            if result < -2**31: return -2**31
            if result > 2**31-1: return 2**31 - 1
            return result
        except:
            return 0

#         # if str == '':
#         #     return 0
#         list1 = str.split()
#         if list1 == []:
#             return 0
#         print(list1)
#         print(list1[0])
#         try:
#             if int(float(list1[0])) > 2**31 - 1:
#                 print('case1')
#                 return 2**31 - 1
#             elif int(float(list1[0])) < -2**31:
#                 print('case2')
#                 return -2 ** 31
#             else:
#                 print('case3')
#                 return int(float(list1[0]))
#         except:
#             return 0
                
        
        """
        :type str: str
        :rtype: int
        """