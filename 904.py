class Solution:
    def totalFruit(self, tree):
        blocks = [(key,len(list(group))) for key,group in itertools.groupby(tree)]
        

        result = i = 0
        while i < len(blocks):
            typeOfFruit = set()
            current_weight = 0
            
            for j in range(i,len(blocks)):
                typeOfFruit.add(blocks[j][0])
                current_weight += blocks[j][1]
                if len(typeOfFruit) >= 3:
                    i = j - 1
                    break
                result = max(result,current_weight)
            else:
                break
        return result
        """
        :type tree: List[int]
        :rtype: int
        """
#The key insight is that when we encounter a 3, we do not need to start from the second element 2 (marked _2_ for convenience); we can start from the first element (_1_) before the 3. This is because if we started two or more elements before, the sequence must have types 1 and 2, and that sequence is going to end at the 3, and thus be shorter than anything we've already considered.        
