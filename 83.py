# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        if head:
            head1 = head
            while head1.next:
                
                if head1.val == head1.next.val:
                    
                    head1.next = head1.next.next
                else:
                    head1 = head1.next
        return head
                


        """
        :type head: ListNode
        :rtype: ListNode
        """