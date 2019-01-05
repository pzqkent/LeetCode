def intToRoman(self,num):
	roman = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
	(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),
	(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
	result = ''
	for couple in roman:
		rest = num // couple[0]
		result += couple[1] * rest
		num -= rest * couple[0]
	return result