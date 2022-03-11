class Solution:
    def minFlips(self, s: str) -> int:
        
        # for string of length say 6 there are only 2 alternationg possible
        # 101 010 or 010 101  lets say our string is 111000 so we just need to count the diff
        # (at positions) b/w our string and results and find the min of them O(n)
        # this approach only takes into account type-2 operation 
        
        # but if we also do type-1 operation then we just move prefix to suffix and then find the diff
        # so the time complexity becomes (n-1)*n (n-1 as n type1 operation would result in the same string)
        
        # O(n2)
        
        # we will reduce the number of comparisons by using sliding window and the complexity would be
        
        # O(N)
        
        size = len(s)
        s= s+s # using this to reduce comaprison in typ1 operation
        
        alt1, alt2 = "", ""
        
        for i in range(len(s)):
            alt1 += "0" if i%2 else "1"
            alt2 += "1" if i%2 else "0"
        
        dif1, dif2 = 0,0
        l=0
        result = len(s)
        for r in range(len(s)):
            if s[r] != alt1[r]:
                dif1+=1
            
            if s[r] != alt2[r]:
                dif2+=1
            
            if (r-l+1)>size:
                if s[l] != alt1[l]: # if there was a difference between them then it has to be reduced before shifting right
                    dif1-=1
            
                if s[l] != alt2[l]:
                    dif2-=1
                
                l += 1
            if (r-l+1)==size:
                result = min(result,dif1,dif2)
        
        return result
            
            
            
        