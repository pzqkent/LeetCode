# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




'''
recursive way
'''
class Solution:
    
    def insertIntoBST(self,root,val):
        self.insertIntoBSThelper(root,val)
        return root
    def insertIntoBSThelper(self, root, val):
        node = root
        if node.val > val:
            if node.left == None:
                node.left = TreeNode(val)
                return
                # return root
            else:
                return self.insertIntoBST(node.left,val)
        else:
            if node.right == None:
                node.right = TreeNode(val)
                return
                # return root
            else:
                return self.insertIntoBST(node.right,val)
            
        
'''
iterative way
'''      
        
        # node = root
        # while node:
        #     if node.val > val:
        #         if node.left == None:
        #             node.left = TreeNode(val)
        #             return root
        #         else:
        #             node = node.left
        #     else:
        #         if node.right == None:
        #             node.right = TreeNode(val)
        #             return root
        #         else:
        #             node = node.right
                
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        