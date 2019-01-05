class Solution(object):
    def romanToInt(self, s):
        new_dic = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        slist = list(s)
        print(slist)
        total = 0
        for i in range(len(slist)):
            if len(slist) == 1:
                total = new_dic[slist[0]]
            elif i == 0:
                if new_dic[slist[i]] >= new_dic[slist[i+1]]:
                    total += new_dic[slist[i]]
                else:
                    total = total + new_dic[slist[i + 1]] - new_dic[slist[i]]
            elif i == len(slist)-1:
                if new_dic[slist[i]] > new_dic[slist[i - 1]]:
                    pass
                else:
                    total = total + new_dic[slist[i]]
            elif new_dic[slist[i]] >= new_dic[slist[i+1]]:
                if new_dic[slist[i]] > new_dic[slist[i-1]]:
                    pass
                else:
                    total = total + new_dic[slist[i]]
            else:
                total = total = total + new_dic[slist[i+1]] - new_dic[slist[i]]
                # if i == 0:
                #     total = total = total + new_dic[slist[i+1]] - new_dic[slist[i]]
                
#                 if new_dic[slist[i]] > new_dic[slist[i - 1]]:
#                     pass
                # else:

            
            print(total)
                


        return total
        """
        :type s: str
        :rtype: int
        """
        