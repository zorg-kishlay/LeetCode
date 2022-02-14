class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        # will solve it with greedy
        # rather than going from 1 to target lets go from target to 1
        
        moves = 0
        
        # we can maximise by using maxDoubles max no of times
        while target>1:
            
            # if target is multiple of 2 and we still have balance of
            # maxDoubles
            if target%2==0 and maxDoubles>0:
                target//=2
                moves+=1
                maxDoubles-=1
                continue 
            
            elif maxDoubles ==0:
                moves+=target-1
                break
            
            # when we have maxDoubles left but the remaining number is
            # not a multiple of 2
            else:
                moves+=1
                target-=1
        
        return moves