# class Solution:
#     def isIsomorphic(self, s, t):
#         return list(map(s.find,s)) == list(map(t.find,t))
#         print(list(zip(s,t)))        
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        
class Solution:
    def isIsomorphic(self,s,t):
        print(set(zip(s,t)))
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))