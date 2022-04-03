class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #graph problem where we want to check if we can visit all nodes starting from node 0
        
        # Time O(N+K) N is no of rooms and k is no keys
        # Space O(N)
        
        visited = set([0])
        
        def dfs(room):
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)
        
        dfs(0)
        return len(visited)==len(rooms)
            
        
            
        