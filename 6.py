class Solution(object):
	def convert(self,s,numRows):
		if numRows == 1:
			return s
		zigzag = ['' for i in range(numRows)]
		row = 0
		step = 1
		for letter in s:
			if row == 0:
				step = 1
			if row == numRows - 1:
				step = -1
			zigzag[row] += letter
			row += step

		return ''.join(zigzag)