class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:    
    
    

        rows = len(image)
        cols = len(image[0])
        original = image[sr][sc]
        def get_neighbours(node):
            r,c = node
            result = []
            for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
                row = r+i
                col =c +j

                if row <0 or row>=rows or col<0 or col>= cols:
                    continue
                
                result.append((row,col))
            
            return result
        

        def bfs(root):
            queue = collections.deque([root])
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            #r,c = root

            while len(queue)!=0:
                node = queue.popleft()
                r,c = node            
                image[r][c]=color
                visited[r][c]=True
                
                for neighbour in get_neighbours(node):
                    ro,co = neighbour
                    if visited[ro][co]:
                        continue
                    if image[ro][co]==original:
                        image[ro][co]=color
                        visited[ro][co]=True
                        queue.append(neighbour)
        
        bfs((sr,sc))
        return image
        