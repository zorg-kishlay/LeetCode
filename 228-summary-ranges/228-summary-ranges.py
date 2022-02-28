class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        
        if N == 0:
            return []
        INF = 10 ** 10
        nums.append(INF)
        result = []
        start = nums[0]
        for i in range(N):
            if nums[i] + 1 != nums[i + 1]:
                end = nums[i]

                if end == start:
                    result.append(f"{start}")

                else:
                    result.append(f"{str(start)}->{str(end)}")

                start = nums[i + 1]
        return result
    
    # O(N) space and time