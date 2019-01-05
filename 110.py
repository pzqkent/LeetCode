# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return abs(self.treeheight(root.left)-self.treeheight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def treeheight(self,root):
        if not root:
            return 0
        else:
            return 1 + max(self.treeheight(root.left),self.treeheight(root.right))