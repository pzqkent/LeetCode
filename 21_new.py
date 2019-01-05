# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        val = sorted(self.traversal(l1) + self.traversal(l2))
        head1 = node = ListNode(0)
        for i in val:
            node.next = ListNode(i)
            node = node.next
        return head1.next
        
    def traversal(self,head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
        """
        思路一：分别遍历两个linked list，然和合并得到的序列，进行排序，然后利用得到的序列生成一个新的linked list
        思路二：同时遍历两个linked list，在同一个node处，将更小的值加入新创建的linked list
        
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """