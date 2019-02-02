class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        elif len(nums) == 0:
            return -1
        
        
        low,high = 0,len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid
            else:
                return mid
        
        if nums[low] == target:
            return low
        else:
            return -1   
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        