class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # O(n*4n) 4 to power n
        
        result = []
        
        number_map ={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        
        def track(index,slate):
            if len(slate) == len(digits):
                result.append("".join(slate))
                return
            
            for ch in number_map[digits[index]]:
                slate.append(ch)
                track(index+1,slate)
                slate.pop()
        
        
        if digits:
            track(0,[])
        
        return result
        