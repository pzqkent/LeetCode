# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        思路一：
        遍历lists 中包含的所有linked list，将得到的结果组合成一个新的list，然后排序，最后利用排序后的值生成新linked list
        """
        # print(lists)
        if lists == []:
            return []
        value = []
        for i in lists:
            value = value + self.traversal(i)
        value.sort()
        return self.new_list(value)

    def traversal(self,head):
        result = []
        # if not head:
        #     return []
        # node = head
        # while node:
        while head:
            result.append(head.val)
            # result.append(node.val)
            head = head.next
            # node = node.next
        return result
    
    def new_list(self,nums):
        if not nums:
            return []
        head1 = ListNode(nums[0])
        node1 = head1
        for i in nums[1:]:
            # head1.next = ListNode(i)
            node1.next = ListNode(i)
            # head1 = head1.next
            node1 = node1.next
        return head1
            
        