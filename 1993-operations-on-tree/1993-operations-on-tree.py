class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        
        self.locked =[None]* len(parent) # basically to store the locked state of node and which user has it
        
        # a parent array parent where parent[i] is the parent of the ith node
        self.child = {i:[] for i in range(len(parent))}
        
        for i in range(1,len(parent)):
            self.child[parent[i]].append(i) # basically adding children of parent[i]
        

    def lock(self, num: int, user: int) -> bool:
        #if a node is locked then return False
        if self.locked[num]:
            return False
        self.locked[num] = user # basically locking the node
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        # only user who locked it is allowed to unlock it
        if self.locked[num]!= user:
            return False
        
        self.locked[num] = None # basically unlocking the node
        return True
        

    def upgrade(self, num: int, user: int) -> bool:
        i = num
        while i!=-1: # parent of root would be -1
            if self.locked[i]: # condition 1 and 3
                return False
            
            i = self.parent[i]
        
        locked, q = 0, deque([num])
        while q:
            n = q.popleft()
            
            if self.locked[n]:
                # if it is locked then unlock it
                self.locked[n]=None #
                locked +=1 # to keep track of locked descendant
            q.extend(self.child[n])
        if locked >0:
            self.locked[num]=user # condition 2 for ugrade
        
        return locked>0
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)