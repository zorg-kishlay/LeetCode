class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dom = list(dominoes)
        
        queue = deque()
        
        for idx,d in enumerate(dom):
            if d!=".":
                queue.append((idx,d))
        
        
        while queue:
            idx,d = queue.popleft()
            
            if d == "L" and idx>0 and dom[idx-1]==".":
                queue.append((idx-1,"L"))
                dom[idx-1]="L"
            
            elif d =="R":
                if idx+1<len(dom) and dom[idx+1] ==".":
                    
                    # with this we also ensure that for each L that we encounter we
                    # have gotten over the previous R
                    if idx+2<len(dom) and dom[idx+2]=="L":
                        queue.popleft() # we don't need to visit this as R and L get balanced
                    
                    else:
                        queue.append((idx+1,"R"))
                        dom[idx+1]="R"
        
        
        return "".join(dom)
    
    # Time and Space: O(N)