class Solution(object):
    def flipAndInvertImage(self, A):
        new_list = []
        for item in A:
            item1 = list(reversed(item))
            # item2 = item1
            
            # print(item2)
            
            for i in range(len(item1)):
                item1[i] = item1[i] ^ 1
            new_list.append(item1)   
            # print item1
        return new_list
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        