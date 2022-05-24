class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        result = 0
        
        stack.append(-1)
        # longest valid parentheses 
        
        # we will store the index of the last valid parentheases,This will help us in calculating size
        # by subtarcting the current index with index of last valid parentheses 
        for i in range(len(s)):
            
            if s[i] == '(': # simply push we don't need to do anything here
                stack.append(i)
            
            else: # when we encounter a closing bracket
                stack.pop(-1)
                if not stack: # stack will be empty when we have a valid parenthesis and the above will pop out the last successfull index so we push the current index to track the current substring
                    stack.append(i)
                else:
                    result = max(result,i-stack[-1])
                
            
        
        return result
        