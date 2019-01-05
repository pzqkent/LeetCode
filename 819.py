class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import re
        from collections import Counter
        newpara = re.split('\W', paragraph.lower())
        a = ' '.join(newpara)
        c = a.split()

        # print c
        # b = c.strip(' ')
        # for word in newpara:
        #     print word
        set1 = set()
        for i in range(len(c)):
            # print c[i];
            set1.add(c[i])
        for word in banned:
            if word in set1:
                set1.remove(word)
            # set1.remove(word)
            
        # set1.remove(banned)
        dic1 = dict()


        for word in set1:
            dic1[word] = 0
        # print dic1
        for word in c:
            if word in set1:
                dic1[word] += 1
        keys = dic1.keys()
        values = dic1.values()
        index1 = values.index(max(values))
        result = keys[index1]
        return result
        
#         print(a)
#         print c


#         # set1 = c
#         print set1

            

        
        
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        