                                                          
# ================================ 
# 传统递归
class Solution:
	def letterCombinations(self,digits):
		out = []
		dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

		if len(digits) == 0:
			return []

		for i in dic[digits[0]]:
			if len(digits) == 1:
				out.append(i)
				if i == dic[digits[0]][-1]:
					return out
			else:
				for j in self.letterCombinations(digits[1:]):
					out.append(i+j)
					if i == dic[digits[0]][-1] and j == self.letterCombinations(digits[1:])[-1]:
						return out


		

