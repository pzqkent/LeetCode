class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return None
        node = head
        length = 0
        while node:
            length += 1
            node = node.next
        if length == 1:
            return []
        node1 = head
        target = length - n
        if target == 0:
            head = head.next
            return head
        counter = 1
        while node1:
            if counter == target:
                try:
                    node1.next = node1.next.next
                    break
                except AttributeError:
                    node1.next = None
                    break
            else:
                node1 = node1.next
            counter = counter + 1
        return head 
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """