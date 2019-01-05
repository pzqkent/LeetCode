# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, left = float('-inf'),right = float('inf')):
        if not root:
            return True
        if root.val >= right or root.val <= left:
            return False
        return self.isValidBST(root.left,left,min(right,root.val)) and self.isValidBST(root.right,max(left,root.val),right)
        """
        :type root: TreeNode
        :rtype: bool
        思路：如果当前节点在父节点左边，它应当小于父节点的值；如果当前节点在父节点的右边，则它应当大于父节点的值
        """
        



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
思路二：based on inorder traversal
'''
class Solution:
    # @param root, a tree node
    # @return a boolean
    # 7:38
    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)