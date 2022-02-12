class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        if x == 0:
            return True
        
        num = str(x)
        
        start =0
        end = len(num)-1
        
        while start< end:
            if num[start] != num[end]:
                return False
            
            start+=1
            end-=1
        
        
        return True
        