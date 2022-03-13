class Solution:
    def decodeString(self, s: str) -> str:
        
        # since the string can be a nested we'll use a stack to insert and pop
        
        stack = []
        
        for ch in s:
            # if we don't find a closing bracket just keep pushing to stack
            if ch !="]":
                stack.append(ch)
            
            # when we find a closing bracket:
            # 1. pop till we get an opening bracket -> this will give us the substring
            # 2. pop once more to get rid of opening bracket
            # 3. pop to get the number
            else:
                sub = ""
                while stack[-1] != "[":
                    # the order here is important else it will be in reverse order
                    sub = stack.pop() + sub
                
                stack.pop()
                
                digit = ""
                
                while stack and stack[-1].isdigit():
                    digit = stack.pop()+digit # this is to handle the case where the digit might be 2 or 3 digit number
                
                # now we just append the sub string to stack digit number of times
                
                stack.append(int(digit)*sub)
        
        return "".join(stack)
        