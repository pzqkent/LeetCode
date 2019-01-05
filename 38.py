class Solution(object):
    def countAndSay(self, n):
        s="1"
        for i in range(1,n):
            nums=[s[0]]#first char to compare the chars after it with it
            values=[1]
            l=len(s)
            for j in range(1,l):
                if s[j]==nums[-1]:
                    
                    #if the last char is the same doesn't change
                    values[-1]+=1
                else:
                    #new char
                    nums.append(s[j])
                    values.append(1)
            #new s
            s=""
            for v,k in zip(values,nums):
                s+=str(v)+k
        return s


        """
        :type n: int
        :rtype: str
        """
        