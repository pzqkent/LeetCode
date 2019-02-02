class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        elif len(nums) == 0:
            return None
        mid = (len(nums) - 1) // 2
        # print(nums[mid-1],nums[mid+1])
        while mid>=1 :
            if nums[mid-1] < nums[mid] < nums[mid+1]:
                if mid + 1 == len(nums) - 1:
                    return mid + 1
                mid = mid + 1
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                mid = mid - 1
            elif nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            else:
                mid = mid - 1
        if nums[0]>nums[1]:
            return 0
        else:
            return 1
                
                
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        