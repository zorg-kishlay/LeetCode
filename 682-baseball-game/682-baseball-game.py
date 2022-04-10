class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        # stack use
        stack =[]
        
        for op in ops:
            
            if op == "+":
                stack.append(stack[-1]+stack[-2]) # appending sum of last 2 indices
                # not checking because question states that there will be atleast 2 elements
            elif op == "C":
                stack.pop()
            
            elif op == "D":
                stack.append(2*stack[-1])
            
            else:
                stack.append(int(op))
        
        
        return sum(stack)
    
    # Time : O(N) space O(N)
            