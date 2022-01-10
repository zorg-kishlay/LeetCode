class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Lenght of substring can't be more than original
        if len(s)>len(t):
            return False
        
        i=j=0
        
        while i<len(s) and j<len(t):
            
            # if substring character is present in original move both indices
            if t[j] == s[i]:
                i+=1
            # if substring character is absent in original move pointer to original indices
            j+=1
        
        # if i hasn’t reached to len(s) means there are characters in s not present in t
        if i != len(s):
            return False
        
        return True
                
        