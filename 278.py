# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if n == 1:
            return 1
        low, high = 1,n
        while low < high:
            mid = (low+high) // 2
            if isBadVersion(mid) == True:
                if isBadVersion(mid-1) == False:
                    return mid
                else:
                    high = mid - 1
            else:
                if isBadVersion(mid+1) == True:
                    return mid + 1
                else:
                    low = mid + 1
        return low
        """
        :type n: int
        :rtype: int
        """