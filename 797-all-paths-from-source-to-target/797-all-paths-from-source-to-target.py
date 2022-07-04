class Solution:
    
    def getAdjMap(self,graph):
        n = len(graph)
        adjMap = {i:[] for i in range(n)}
        
        for i in range(n):
            adjMap[i].extend(graph[i])
        
        return adjMap
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adjMap = self.getAdjMap(graph)
        n = len(graph)
        result = []
        #visited = [-1]*n
        def dfs(node,slate):
            #visited[node]=1
            #slate.append(node)
            if node==n-1:
                result.append(slate[:])
                #slate.pop()
                #return
            else:
                for ngb in adjMap[node]:
                    #if visited[ngb]==-1:
                    slate.append(ngb)
                    dfs(ngb,slate)
                    slate.pop()
        
        #for i in range(n):
            #if visited[i]==-1:
        dfs(0,[0])
        
        return result