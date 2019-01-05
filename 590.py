"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):



    
    ########################################
    #递归
        # result = []
        # def dfs(node):
        #     if not node:
        #         return 
        #     for child in node.children:
        #         dfs(child)
        #     result.append(node.val)
        # dfs(root)
        # return result
    #########################################
    # 重复循环
    
        if not root:
            return []
        result = collections.deque([])  
        '''
        creat a two-side queue
        '''
        stack = [root]
        while stack:
            u = stack.pop()
            result.appendleft(u.val)
            for child in u.children:
                stack.append(child)
        return list(result)
    ####3#####################################
    
    
    

        """
        :type root: Node
        :rtype: List[int]
        """

