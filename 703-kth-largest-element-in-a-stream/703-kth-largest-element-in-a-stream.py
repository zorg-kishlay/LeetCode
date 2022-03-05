class KthLargest:

    # we will be using a min heap of size k why min heap?
    # because lets say we have a greater number coming in then we would want to remove the
    # smallest element in the heap
    # also for 3rd larget element in the stream we would need tp just remove min which will be
    # O(1) operation
    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        # convert minheap to heap
        heapq.heapify(self.minheap)
        
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)

        # O(NlogN)
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        
        # if len(minheap)< k we don't need to pop
        
        if len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        
        return self.minheap[0] # minheap in our case will have K largest element at 0
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)