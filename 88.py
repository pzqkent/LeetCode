class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(0, len(nums2)):
            nums1.insert(m+i, nums2[i])
            nums1.pop(-1)
        
        nums1.sort()
        # print nums1
#         for i in range(0, len(nums2)-1):
#             for j in range(0, len(nums1)-1):
#                 if nums2[i] >= nums1[j]:
#                     nums1.insert(j+1,nums2[i])
#                     nums1.pop(-1)
#                     break
#                 else:
#                     nums1.insert(i,nums2[i])
#                     nums1.pop(-1)
#                     break
                    
#         for i in range(0, len(nums2)-1):
#             low = 0
#             high = m-1
#             while low<=high:
#                 mid = (low + high) / 2
#                 if nums2[i] == nums1[mid]:
#                     nums1.insert(mid,nums[i])
#                     nums1.pop(-1)
#                     break
#                     # low = mid + 1
#                 elif nums2[i] > nums1[mid]:
                    
#                 else:
#                     nums1.insert(mid)
                    
                    

                
        
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        