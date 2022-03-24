class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # O(NlogN) time
        people.sort()
        result = 0
        
        start,end = 0, len(people)-1
        
        # to minimize the number of boats the largets value has to pair up with the
        # smallest value if it can't then there is no point in pairing it up with a greater value
        while start<=end:
            # check if smallest and largest can form a pair
            if people[start]+people[end]<=limit:
                # if they do we can no move on to the next smallest largest pair
                start+=1
                end-=1
            
            else:
                # if not we increment result by 1(since the largest element has to travel solo just like you) and check for the next largest element
                end -=1
            
            result+=1
        
        
        return result
            
            
        