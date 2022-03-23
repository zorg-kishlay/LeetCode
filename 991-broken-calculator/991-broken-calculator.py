class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        
        # O(log(target)) time

        # since we have to find minm no of steps to reach target lets go
        # top-down by reducing target based so for target we'll have 2 operations
        # 1. divide target/2
        # 2. add 1 to target
        
        result = 0
        
        while target>startValue:
            if target % 2 != 0:
                target = target+1  # since for odd number we anyway won't get a round of digit when diving by 2
            
            else:
                target = target//2 # whenever even we can easily divide by 2 for max effect
            
            result+=1 # whatever we do we have are doing an operation
        
        
        remainder = startValue-target # for cases where target<startvalue we can only do 1 operation i.e adding 1 to target
        
        return result+remainder
        