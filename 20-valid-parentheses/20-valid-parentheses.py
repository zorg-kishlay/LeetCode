class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_dict ={
            "]":"[",
            ")":"(",
            "}": "{",
        }
        stack = []
        opening = ("{","[","(")
        closing = ("}",")","]")        
        for ch in s:
            if ch in opening:
                stack.append(ch)
            
            elif ch in closing:
                if len(stack) == 0: # if we just have 1 closing bracket
                    return False
                
                if stack.pop()!=bracket_dict[ch]:
                    return False
        
        if len(stack)>0: #if in the end we have only empty brackets
            return False
        
        return True
                