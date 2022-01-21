class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[start] != val:
                start += 1
            elif nums[start] == val and nums[end] == val:
                end -= 1
            elif nums[start] == val and nums[end] != val:
                nums[start], nums[end] = nums[end], nums[start]
                # while nums[end - 1] != val:
                #     end -= 1
                start += 1
            # else:
            #     start += 1

        #print(nums)
        return start
        