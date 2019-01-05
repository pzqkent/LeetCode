# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # while (root.val - p.val) * (root.val - q.val) > 0:
        #     root = (root.left,root.right)[p.val > root.val]
        # return root
    
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root
        """
        Just walk down from the whole tree's root 
        as long as both p and q are in the same 
        subtree (meaning their values are both smaller or 
        both larger than root's). This walks straight from 
        the root to the LCA, not looking at the rest of the tree, 
        so it's pretty much as fast as it gets. 
        A few ways to do it:
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        