class Solution(object):
    def shortestToChar(self, S, C):
        index1 = []
        for i in range(len(S)):
            if S[i] == C:
                index1.append(i)
        # print index1
        result = []
        for i in range(len(S)):
            distance = len(S)
            for j in range(len(index1)):
                distance = min(distance, abs(index1[j] - i))
            result.append(distance)
            
        return result        
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        