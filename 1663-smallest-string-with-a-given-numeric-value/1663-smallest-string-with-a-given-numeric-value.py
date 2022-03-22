class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        # simple appraoch

        # the lexicographically smallest string with length n is "aaa..n times"
        
        # since we want lexicographically smallest string and in dictionary left most bit has
        # precedence so whatever we need to add we should be adding to the right side
        
        
        # we will create a sting of a of length n
# then we do iterations from the end and try to maxmize the value in the end

        result = ['a' for i in range(n)]
        k = k-n # since we are already adding n charcters
        
        while k>0:
            n-=1
            result[n]= chr(ord(result[n])+min(25,k)) # if k>25 we are simply adding it to the string for maximizing it
            
            # for ex for k = 50 and n=4 we can have aaaz (that maximizes the use in end)
            k-=min(25,k) # subtract from k whatever we are adding in the result
        
        
        return "".join(result)
            
    
        