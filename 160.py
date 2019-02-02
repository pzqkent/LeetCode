# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        def get_len(head):
            curr = head
            l = 0
            while curr:
                l += 1
                curr = curr.next
            return l
        lA = get_len(headA)
        lB = get_len(headB)
        
        if lA > lB:
            curr1 = headA
            curr2 = headB
        else:
            curr1 = headB
            curr2 = headA
        for i in range(abs(lA - lB)):
            curr1 = curr1.next
    
        while curr1:
            if curr1 == curr2:
                return curr1

            curr1 = curr1.next
            curr2 = curr2.next

        return None
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        