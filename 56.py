# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):

        intervals = sorted(intervals,key = lambda x : x.start) #对intervals 进行排序
        i = 0 #指针1指向第一个interval
        
        while i < len(intervals)-1:
            j = i + 1
            while j < len(intervals):#指针2指向当前指针1对应interval的下一个interval
                if intervals[j].start<=intervals[i].end<=intervals[j].end: #满足这个条件则重新对指针1指向的interval重新赋值
                    intervals[i].end = intervals[j].end
                    del intervals[j]#删除指针2对应的interval

                    # j = j
                elif intervals[j].end <= intervals[i].end:
                    del intervals[j]

                    # j=j
                else:#如果指针2对应的interval不满足上面两个条件，则指针1指向当前指针2所在的位置
                    i = j
                    break

  
        return intervals
                
                
            
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        