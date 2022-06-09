class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        if len(numbers)==2:
            return [1,2]
        
        left = 0
        right = len(numbers)-1
        result= []
        
        while left<right:
            add = numbers[left]+numbers[right]
            
            if add < target:
                left+=1
            
            if add > target:
                right-=1
            
            elif add == target:
                result.append(left+1)
                result.append(right+1)
                break
        
        return result
        