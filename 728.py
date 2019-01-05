class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        counter = 0
        for i in range(left,right+1):
            ilist = list(str(i))
            for num in ilist:
                if int(num) == 0:
                    break
                elif i % int(num) == 0:
                    counter += 1

            if counter == len(ilist):
                result.append(i)
            counter = 0

        return result
            

        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        