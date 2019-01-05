class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        result = []
        c1 = Counter(nums)
        result_list = c1.most_common(k) '''[(),(),()] = [tuple1,tuple2,tuple3]'''
        for item in result_list:
            result.append(item[0])
        return result
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        