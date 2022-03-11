class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # can take count and then add elements to a max heap and then pop time: - O(KlogN)
        
        # we will use bucket sort Time & Space = O(N)
        # general bucket sort won't work because our array has no range
        
        # we can have buckets upto len(array) as even the max an element can occur is len(array)
        # in which case it'll be present in all elements
        
        # and then we can return from the end
        
        count_dict = {}
        result = []
        bucket =[[] for _ in  range(len(nums)+1)]
        
        # count the occurence of each element
        for num in nums:
            count_dict[num] = 1+ count_dict.get(num,0)
        
        # for number and count in the map
        # and the count as the index we will store the number that occurs count number of times
        for num,count in count_dict.items():
            bucket[count].append(num)
        
        
        for idx in range(len(bucket)-1,-1,-1):
            for num in bucket[idx]: # is skipped if no element is present
                result.append(num)
                
                if len(result) == k: # guranteed to happen so no need to write outside loop
                    return result
            
        