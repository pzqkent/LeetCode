# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        
        '''
        iterative
        '''
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return []
    
    
    
        
        '''
        recursive
        '''
        # if root:
        #     if root.val == val:
        #         return root
        #     elif root.val < val:
        #         return self.searchBST(root.right,val)
        #     else:
        #         return self.searchBST(root.left,val)
        # return []
        
        
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """