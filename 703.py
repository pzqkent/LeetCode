class KthLargest:

    def __init__(self, k, nums):
        import heapq
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        这道题要用堆来做。
        从小到大排序后从右往左数第k大的数字。python的heap是小根堆，如果维持一个大小为k的heap的话，那么最小的数字（第一个数字）就是最终答案。
        后续的数字只需要和最小的数字self.nums[0]比较大小就好。如果当前的堆的大小小于k，则将新元素入堆；否则，当前堆的大小一定是k（因为初始化的         时候如果nums的长度大于k，已经将堆裁剪为大小为k的堆了），此时需要比较当前的val和self.num[0]的关系，如果val<self.nums[0]，则保持堆不         变；如果val大，则弹出堆中的最小值，将val入堆。
        python中可以直接用heapq.heapreplace(data,val)，比先heap.pop()再heapq.push()的速度要快得多。

        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)