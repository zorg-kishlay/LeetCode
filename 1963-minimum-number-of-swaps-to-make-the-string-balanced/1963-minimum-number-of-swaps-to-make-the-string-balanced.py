class Solution:
    def minSwaps(self, s: str) -> int:
        
        # we will keep max of extra closing brackets and find its ceil thendivide by2
        # why? swapping 1 closed bracket with open bracket actually cancels out 2 closing bracket
        # 1 being swapped and 1 whose open brancket we have added
        
        
        #  ]]] [[[  max closing = 3
        # if we swap 0 index with 3 index then clos is turned to 1
        
        close, maxClose = 0,0
        
        for c in s:
            if c == "[":
                close -= 1
            else:
                close += 1
            
            maxClose = max(close,maxClose)
            
        result = (maxClose+1)//2
        return result