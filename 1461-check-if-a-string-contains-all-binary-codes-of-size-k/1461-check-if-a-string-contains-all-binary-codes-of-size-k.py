class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        # we can generate all substrings of s and then do a lookup for length k substrings 
        # in this list O(2^n)*O(N)
        
        # optimised:- rather than appending all substrings we can try for substrings of length k
        # and if the size is equal to 2^k then its True
        
        
#         result = set()
        
#         def backtrack(st,i,slate):
#             if len(slate)==k:
#                 result.add("".join(slate))
#                 return
            
#             if i == len(s):
#                 return
            
#             backtrack(st,i+1,slate)
#             slate.append(st[i])
#             backtrack(st,i+1,slate)
#             slate.pop()
        
#         backtrack(s,0,[])
#         print(result)
        
#         for el in result:
#             if el not in s:
#                 return False
        
#         return True if len(result) else False
        
       # return len(result)==pow(2,k)
        
        result = set()
        
        for i in range(0,len(s)-k+1):
            result.add(s[i:i+k])
        
        return len(result)==pow(2,k)
        
        