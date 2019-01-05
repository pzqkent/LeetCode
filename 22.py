class Solution:
	def generateParenthesis(self,N):
		ans = []
		def backtrack(s='',left=0,right=0):
			if len(s) == 2 * N:
				ans.append(s)
			if left < N:
				backtrack(s+'(',left+1,right)
			if right < left:
				backtrack(s+')',left,right+1)
		backtrack()
		return ans