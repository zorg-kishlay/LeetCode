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
        
        def track(index,current):
            if len(current) == len(digits):
                result.append(current)
                return
            
            for ch in number_map[digits[index]]:
                track(index+1,current+ch)
        
        
        if digits:
            track(0,"")
        
        return result
        