class Solution:
    def isSymmetric(self,root):
        if not root:
            return True
        else:
            return self.ismirror(root.left,root.right)
        
    def ismirror(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val == right.val:
            return self.ismirror(left.left,right.right) and self.ismirror(left.right,right.left)
        else:
            return False

            
class Solution:
	def isSymmetric(self,root):
		if root is None:
			return True

		stack = [[root.left,root.right]]
		while len(stack)>0:
			pair = stack.pop(0)
			left = pair[0]
			right = pair[1]

			if left is None and right is None:
				continue
			if left is None or right is None:
				return False
			if left.val == right.val:
				stack.insert(0,[left.left,right.right])
				stack.insert(0,[left.right,right.left])

			else:
				return False
		return True


class Solution:
	def isSymmetric(self,root):
		def isSym(left,right):
			if not left and not right:
				return True
			if left and right and left.val == right.val:
				return isSym(left.left,right.right) and isSym(left.right,right.left)
			return False

		return isSym(root,root)