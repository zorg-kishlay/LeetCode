class Solution:
    def findIn(self,nums,el):
        for i in range(len(nums)):
            if nums[i]==el:
                return i
    def twoSum(self, nums, target: int):
        dic = {}

        result = []
        for i in range(len(nums)):
            tr = target - nums[i]
            if tr in dic:
                result.append(i)
                result.append(self.findIn(nums,tr))
            else:
                dic[nums[i]] = 1


        return result