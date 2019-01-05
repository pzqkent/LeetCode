# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        while head:
            if head.next == 'test':
                return True
            next_step = head.next
            head.next = 'test'
            head = next_step
        return False
        """
        :type head: ListNode
        :rtype: bool
        """
        
    # def hasCycle(self, head):
    #     # Burning bridges
    #     while head != None:
    #         if head.next == "burnt":
    #             return True
    #         next_step = head.next
    #         head.next = "burnt"
    #         head = next_step
    #     return False