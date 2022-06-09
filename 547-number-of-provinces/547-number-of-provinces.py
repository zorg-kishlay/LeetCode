class Solution:
    
    def adjMapCreate(self,n,isConnected):
        adjmap ={}
        for i in range(n):
            adjmap[i]=[]
        
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if isConnected[i][j]==1:
                        adjmap[i].append(j)
                        adjmap[j].append(i)
        
        return adjmap
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        n = len(isConnected)
        adjmap = self.adjMapCreate(n,isConnected)
        visited = [-1]*n
        
        def dfs(node):
            visited[node]=1
            for ngb in adjmap[node]:
                if visited[ngb]==-1:
                    dfs(ngb)
        
        provinces= 0
        
        for i in range(n):
            if visited[i]==-1:
                provinces+=1
                dfs(i)
        
        return provinces
        