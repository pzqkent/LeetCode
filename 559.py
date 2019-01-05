class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        depth = 0
        stack = [root]
        while stack:
            next_level = []
            while stack:
                node = stack.pop()
                if node.children:
                    next_level += node.children #此处不能使用 append method
            stack = next_level
            depth += 1
        return depth