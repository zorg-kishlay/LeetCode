class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # lets send all of them to the first city and then calculate the sum
        # next we can get difference between cost of city b and city a and subtract the
        # n least differences.

        # This would be simlilar to getting a refund
        
        
        #cost_for_a = [a for a,b in costs] # [10,30,400,30]
        difference = [b-a for a,b in costs] # [10,170,-350,-10]
        
        # now take sum for all costs_for_a
        sum_a = sum([a for a,b in costs])
        sum_b = sum(sorted(difference)[:len(costs)//2]) # basically taking n values
        
        
        
        return sum_a + sum_b
    
    # time : O(nlogn) space O(n) # can get rid of cost_for_a by taking sum at the first place only
        