class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # append to heap
        
        for idx,stone in enumerate(stones):
            stones[idx]=-stone
        
        heapify(stones)
        while stones:
            largest_stone = -heappop(stones)
            
            # if we have only 1 largest stone left
            if not stones:
                return largest_stone
            
            second_largest_stone = -heappop(stones)
            if largest_stone>second_largest_stone:
                heappush(stones,second_largest_stone-largest_stone) # instead of doing subtraction we rather did negative subtarction
                
        
        return 0 # coming here means no elements in heap
    # O(NlogN)