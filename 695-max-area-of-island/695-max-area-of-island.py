class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # create a visited array so that we need to revisit a node
        visited = [[False for value in row] for row in grid]
        size = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                curr_size = self.traversenodes(grid,i,j,visited)
                size = max(size,curr_size )
        
        return size
        
    
    
    def traversenodes(self, grid,i,j,visited):
        
        # array to keep track of nodes to be visited
        nodesToExplore=[[i,j]]
        countForCurrentNode = 0
        
        while len(nodesToExplore):
            current = nodesToExplore.pop()
            i = current[0]
            j = current[1]
            
            # if we revisit a node in current setup and don't
            # continue might cause infinite loop
            if visited[i][j]:
                continue
            
            # mark node as visited
            visited[i][j] = True
            
            # no point in going forward
            if grid[i][j] == 0:
                continue
            
            countForCurrentNode += 1
            # get all unvisted neighbours for current node
            unvistedNodes = self.getUnvisitedNegihbours(grid,i,j,visited)
            
            for nodes in unvistedNodes:
                nodesToExplore.append(nodes)
        
        return countForCurrentNode
            
    
    def getUnvisitedNegihbours(self,grid, i,j,visited):
        
        unvistedNodes = []
        if i>0 and not visited[i-1][j]:
            unvistedNodes.append([i-1,j])
        
        if j>0 and not visited[i][j-1]:
            unvistedNodes.append([i,j-1])
        
        if i<len(grid)-1 and not visited[i+1][j]:
            unvistedNodes.append([i+1,j])
        
        if j<len(grid[0])-1 and not visited[i][j+1]:
            unvistedNodes.append([i,j+1])
        
        return unvistedNodes