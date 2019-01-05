class Solution(object):
    def binaryGap(self, N):
        nb = bin(N)[2:]
        list1 = []
        distance = 0
        # print(nb)
        for i in range(len(nb)):
            if nb[i] == '1':
                list1.append(i)
        # print list1
        for i in range(len(list1)):
            if i == len(list1)-1:
                break
            distance = max(abs(list1[i] - list1[i + 1]), distance)
        return distance
                
        """
        :type N: int
        :rtype: int
        """
        