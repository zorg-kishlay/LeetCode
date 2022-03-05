class Solution:
    def numTrees(self, n: int) -> int:
        
        # Time O(N2) space O(N)
        
        # we know for 0 we can have 1 subtress for 1 we can have 1 subtree
        # for 2 we can have 2 subtress
        
        # numTress[4] = numTress[0] * numTress[3]
          #            + numTress[1] * numTress[2]
         #             + numTress[2] * numTress[1]
        #              + numTress[3] * numTress[0]
        
        # we are calculating all possible combinations with each element as root
        
        dp_tree = [1] * (n+1) # since subtree(0)=1 and subtree(1)=1
        
        for nodes in range(2,n+1):
            result = 0
            for root in range(1,nodes+1):
                left = root-1 
                right = nodes - root
                result += dp_tree[left] * dp_tree[right]
                
            dp_tree[nodes] = result # caching it to be used in further calculations
            
        return dp_tree[-1]
        
        
        