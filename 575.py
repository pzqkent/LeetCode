class Solution(object):
    def distributeCandies(self, candies):
        # list1 = []
        # len1 = len(candies)
        # for item in candies:
        #     if item in list1:
        #         pass
        #     else:
        #         list1.append(item)
        #         # i = i + 1
        # return min(len1/2, len(list1))
        new_set = set(candies)
        return min(len(candies)/2, len(new_set))
        """
        :type candies: List[int]
        :rtype: int
        """
        