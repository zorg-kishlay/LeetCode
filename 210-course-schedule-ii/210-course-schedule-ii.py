class Solution:
    
    def getAdjMap(self, numCourses, prerequisites):
        
        adjMap = {i:[] for i in range(numCourses)}
        
        for dest,src in prerequisites:
            adjMap[src].append(dest)
        
        return adjMap
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjMap = self.getAdjMap(numCourses, prerequisites)
        visited = [-1]*numCourses
        arrival = [-1]*numCourses
        dept = [-1]*numCourses
        #parent = [-1]*numCourses
        result = []
        timestamp= 0
        def dfs(node):
            visited[node]=1
            arrival[node]=timestamp+1
            
            for ngb in adjMap[node]:
                if visited[ngb]==-1:
                    if dfs(ngb):
                        return True
                
                else:
                    if dept[ngb] == -1: # implies we are at ancestor node
                        return True
            
            dept[node]=timestamp+1
            result.append(node)
            return False
        
        for i in range(numCourses):
            if visited[i]==-1:
                if dfs(i):
                    return []
        result.reverse()
        return result