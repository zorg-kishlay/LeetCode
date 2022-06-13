class Solution:
    
    def getAdjMap(self,n,graph):
        adjMap ={i:[] for i in range(n)}
        
        for i in range(len(graph)):
            adjMap[i].extend(graph[i])
    
        return adjMap
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        # trying to solve using BFS.
# the base logic is to check for cycles with odd length
        
    # Section 1:- Graph creation
        n = len(graph)
        adjMap=self.getAdjMap(n,graph)
        
        visited =[-1]*n
        parent = [-1]*n
        distance = [-1]*n # this is to track on which level the cross edge is because odd length of cycle is only possible when cross edge it at same level
        
        # Section 2 BFS or DFS
        def bfs(source):
            q= []
            q.append(source)
            distance[source]=0
            visited[source]=1
            
            while q:
                node = q.pop(0)
                for ngb in adjMap[node]:
                    if visited [ngb]==-1: # not yet visited Tree Node
                        parent[ngb]=node
                        visited[ngb]=1
                        distance[ngb]=1+distance[node]
                        q.append(ngb)
                    
                    else: # cross edge found
                        
                        if ngb!=parent[node]: # cycle detected This can be removed as parent will be 1 level above child
                            if distance[ngb]==distance[node]:
                                return True # basically we have an odd lenth cycle so graph is not bipartite
            return False
                       
            # Section 3 Outer loop
            
        for v in range(n):
            if visited[v]==-1:
                if bfs(v):
                    return False
            
        return True
        