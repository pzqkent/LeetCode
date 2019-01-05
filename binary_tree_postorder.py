class Solution:
    def postorderTraversal(self, root):
        stack = [root]
        res = []
        if not root:
            return []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
        """
        :type root: TreeNode
        :rtype: List[int]
        """
# 思路：因为preorder是按照根，左子树，右子树的顺序来遍历的；而postorder是按照左，右，根的顺序来遍历。
# 所以我们可以将preorder的遍历代码修改为使用根，左，右的遍历的遍历顺序，然后将的到的序列反转即可得到结果。