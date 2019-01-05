class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        output = []
        for i in range(len(findNums)):
            counter = 0
            for j in range(nums.index(findNums[i])+1,len(nums)):
                if nums[j] > findNums[i]:
                    output.append(nums[j])
                    break
                else:
                    counter += 1
            if counter == len(nums) - (nums.index(findNums[i]) + 1):
                output.append(-1)
        return output
            
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        