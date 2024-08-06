class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # BFS Solution
        rows = len(grid)
        cols = len(grid[0])
        def get_neighbours(node):
            result =[]
            r,c = node
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                row = r+i
                col = c+j

                if row<0 or row>=rows or col<0 or col>=cols:
                    continue
                result.append((row,col))
            
            return result
        
        def bfs(root):
            queue= collections.deque([root])

            while len(queue)!=0:
                node = queue.popleft()

                for neighbour in get_neighbours(node):
                    r,c = neighbour

                    if grid[r][c] == "0":
                        continue
                    queue.append(neighbour)
                    grid[r][c]="0"
        
        count=0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j]=="0":
                    continue
                
                bfs((i,j))
                count+=1
        
        return count
        