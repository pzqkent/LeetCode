class Solution(object):
    def threeSumClosest(self, nums, target):
        solution = 0
        nums.sort()
        if len(nums) <= 3:
            return sum(nums)

        for i in range(len(nums) - 1):
            # print('i',i)

            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                diff = max(val,target) - min(val,target)
                # print('diff',diff)
                if diff == 0:
                    return val
                else:
                    if i == 0 and left == 1 and right == len(nums) - 1:
                        mindiff = diff
                        solution = val
                    # print(diff,mindiff)
                    if diff < mindiff:
                        
                        mindiff = diff
                        solution = val
                    # print('mindiff',mindiff)
                    if val < target:
                        left += 1
                    else:
                        right -= 1
        return solution