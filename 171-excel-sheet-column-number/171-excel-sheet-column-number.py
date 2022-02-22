class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        offset =0
        
        n = len(columnTitle)
        
        for i in range(n):
            offset += 26 **i
        
        ans = 0
        for c in columnTitle:
            ans = ans * 26
            ans+= (ord(c)-ord('A'))
        
        return offset + ans
        