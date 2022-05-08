class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        # Simple backtracking question same approach of a helper and parent function call
        # We will maintain a mutuable slate/temporary result character array so that the internal
        # node worker doesn't have to create a new string for each of its iteration
        
        
        result= []
        
        def helper(st,idx,slate):
            
            # base case root level worker simply collects and appends to the o/p
            if idx == len(st):
                result.append("".join(slate))
                return
            
            # recursive code for internal node workers
            
            # if we encounter a digit we simply need to add it to the slate we only have 1 option here
            if (st[idx]).isdigit():
                slate.append(st[idx]) # step1
                helper(st,idx+1,slate)
                slate.pop()  # step 2
                
                # step 1 and 2 always go together pop whatever you are appending so that
                # the parent can send correct base case to the right child
                
            # else if we encounter an alphabet we have 2 options 1 for upper and 1 for lower
            else:
                slate.append((st[idx]).upper())
                helper(st,idx+1,slate)
                slate.pop()
                slate.append((st[idx]).lower())
                helper(st,idx+1,slate)
                slate.pop()
        
        helper(s,0,[])
        return result
    
    # Time:- O(n*2^n) -> 2^n leaf nodes and for each node we do a join operation n
    # Space:- O(n*2^n) -> 2^n o/ps of size n each
        