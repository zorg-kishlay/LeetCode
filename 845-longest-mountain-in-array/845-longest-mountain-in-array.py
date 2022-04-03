class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        size,result= len(arr)-1,0
        
        state=0 # state 0 implies we are starting and should expect next element to be > then prev
        #state=1 implies we are on an icreasing seq and state=2 implies we are on a decreasing seq
        length=1
        for idx in range(size):
            if state in [0,1] and arr[idx+1]>arr[idx]:
                state,length=1,length+1
            
            # this means we were on dec sequence and it was broken now
            # if we take an example at this state we are actually already considering 2 elements
            elif state ==2 and arr[idx+1]>arr[idx]:
                state,length = 1,2
            
            # this is the only state where it is an eligble mountain array
            elif state in [1,2] and arr[idx+1]<arr[idx]:
                state,length=2,length+1
                result = max(result,length)
            else:
                state,length=0,1
        
        
        return result
            
        