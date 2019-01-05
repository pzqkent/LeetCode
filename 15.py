class Solution(object):
	def threeSum(self,nums):
		solution = []
		nums.sort()
		for i in range(len(nums)-1):
			left = i + 1
			right = len(nums) - 1

			if nums[i] > 0:
				return list(set(solution))
            #如果指针i所在的数字已经大于0，则nums[i] + nums[left] + nums[right] 必定大于0
			if i > 0 and nums[i] == nums[i-1]:
				continue
            # 消除连续重复数字的影响
			while left < right:
				val = nums[i] + nums[left] + nums[right]
				if val == 0:
					solution.append((nums[i],nums[left],nums[right]))
					left += 1
					right -= 1
				elif val < 0:
					left += 1
				else:
					right -= 1
		return list(set(solution))