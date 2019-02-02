# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def getCloneNode(self,node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = RandomListNode(node.label)
                return self.visited[node]
        
        return None
    
    def copyRandomList(self, head):
        if not head:
            return head
        
        old_node = head
        new_node = RandomListNode(old_node.label)
        self.visited[old_node] = new_node
        
        while old_node:
            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)
            
            
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]
        

        
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """