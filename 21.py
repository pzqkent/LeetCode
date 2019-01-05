# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        current1 = l1
        current2 = l2
        list1 = []
        while current1 or current2:
            if current1 == None:
                pass
            else:
                list1.append(current1.val)
                current1 = current1.next
            if current2 == None:
                pass
            else:
                list1.append(current2.val)
                current2 = current2.next
        
        list1.sort()
        l3 = ListNode(list1[0])
        current3 = l3
        
        i = 0
        
        while current3:
            # current3.value = list1[i]
            current3.next = ListNode(list1[i + 1])
            current3 = current3.next
            
            i += 1
            # print(i, len(list1))
            if i >= len(list1)-1:
                break
        return l3
    

        # print(len(l1))
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        