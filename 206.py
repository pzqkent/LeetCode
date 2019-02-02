# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev
        """
        :type head: ListNode
        :rtype: ListNode
        """
# While you are traversing the list, change the current node's next pointer to point to its previous element. Since a node does not have reference to its previous node, you must store its previous element beforehand. You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!
# public ListNode reverseList(ListNode head) {
#     ListNode prev = null;
#     ListNode curr = head;
#     while (curr != null) {
#         ListNode nextTemp = curr.next;
#         curr.next = prev;
#         prev = curr;
#         curr = nextTemp;
#     }
#     return prev;
# }