class Solution(object):
    def moveZeroes(self, nums):
        counter = 0
        while nums:
            try:
                a = nums.index(0)
            except ValueError:
                break
            else:
                counter += 1
                nums.remove(0)
        for i in range(counter): nums.append(0)
                