# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        if head == None:
            return True
        # import math
        current = head
        list1 = []
        while current:
            list1.append(current.val)
            # print(current.val)
            current = current.next
            # print(type(current))
        # print(list1)
        # print(list1[len(list1) // 2])
        # print(list1[:len(list1) // 2])
        a = list1[:len(list1)//2]
        b = list1[len(list1) // 2]
        a.append(b)
        # print(type(a))
        # print('type b =', type(b))
        # print(a,b)
        # print('a append b = ',a)
        # print(list1[len(list1) // 2 + 1])
        if list1[:len(list1)//2] == list1[-1:len(list1)//2-1:-1] or len(list1) == 1:
            # print(111)
            return True
        elif len(list1) == 1:
            # print(222)
            return True
        elif len(list1) % 2 == 1 and a == list1[-1:len(list1)//2-1:-1]:
            # print(333)
            return True
            # if :
            #     return True
        else:
            # print(444)
            return False
            
        """
        :type head: ListNode
        :rtype: bool
        """
        