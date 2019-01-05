# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

    
class Solution(object):
    def middleNode(self, head):
        list1 = [head]
        while list1[-1].next:
            list1.append(list1[-1].next)
        # print list1
        return list1[len(list1) / 2]
        """
        :type head: ListNode
        :rtype: ListNode
        """