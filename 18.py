# 解法1:形同3sum问题，在3指针外再增加一层循环 O(N^3) 时间复杂度

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans =set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                rem = target - nums[i] - nums[j]
                l,r = j + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] == rem:
                        ans.add(tuple([nums[i],nums[j],nums[l],nums[r]]))
                        l += 1
                    elif nums[l] + nums[r] < rem:
                        l += 1
                    else:
                        r -= 1
        return sorted([list(x) for x in ans])
# ====================================================================
# 解法2:利用哈希表进行求解，用空间复杂度换取时间复杂度
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numlen,res,adict = len(nums),set(),{}

        # 如果输入数字不够直接返回空列表
        if numlen < 4:
            return []

        # 构建哈希表，如对于num=[1,2,3,2]来说，dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)], 5:[(1,2),(2,3)]}
        nums.sort()
        for i in range(numlen):
            for j in range(i+1,numlen):
                if nums[i]+nums[j] not in adict:
                    adict[nums[i]+nums[j]] = [(i,j)]
                else:
                    adict[nums[i]+nums[j]].append((i,j))

        for i in range(numlen):
            for j in range(i+1,numlen-2):
                digit = target - nums[i] - nums[j]
                if digit in adict:
                    for item in adict[digit]:
                        if item[0] > j:
                            res.add((nums[i],nums[j],nums[item[0]],nums[item[1]]))
        return [list(k) for k in res]
