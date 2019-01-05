class Solution(object):
	def checkPerfectNumber(self,num):
		if num <= 1:
			return False

		return sum(self.getFactors(num)) == num

	def getFactors(self,num):
		sqrt_num = int(math.sqrt(num))
		factors = set([1])

		for i in range(2,sqrt_num+1):
			if num % i == 0:
				factors.add(i)
				factors.add(num/i)
		return factors