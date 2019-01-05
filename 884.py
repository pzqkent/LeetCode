class Solution(object):
    def uncommonFromSentences(self, A, B):
        result = []
        alist = A.split(' ')
        blist = B.split(' ')
        # print(alist)
        # print(blist)
        # if blist[1] in alist:
        #     print 'gg'
            
#         for word in alist:
#             if word not in alist1
#             if word not in blist:
#                 result.append(word)
        for i in range(len(alist)):
            alist1 = alist[:]
            # print i
            # print alist
            # print alist1
            alist1.pop(i)
            if alist[i] not in alist1:
                if alist[i] not in blist:
                    result.append(alist[i])
                    
        for i in range(len(blist)):
            blist1 = blist[:]
            blist1.pop(i)
            if blist[i] not in blist1:
                if blist[i] not in alist:
                    result.append(blist[i])
#         for word in blist:
#             if word not in alist:
#                 result.append(word)

                
        return result
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        