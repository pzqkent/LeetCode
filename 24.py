class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = new_head = ListNode(0)
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            pre.next = tmp
            pre = head
            head = head.next
        return new_head.next
--------------------- 




class Solution:
    def swapPairs(self, head):
        pre,pre.next = self,head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next,b.next,a.next = b,a,b.next
            pre = a
        return self.next
'''
go from pre -> a -> b -> b.next to pre -> b -> a -> b.next
'''
 
