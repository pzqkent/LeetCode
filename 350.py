from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        return list((counter1&counter2).elements())
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        