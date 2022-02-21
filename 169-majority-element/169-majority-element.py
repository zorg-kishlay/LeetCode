class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        major = nums[0]
        count = 1

        for ele in nums:
            if ele == major:
                count += 1

            elif ele != major:
                count -= 1

            if count == 0:
                major = ele
                count = 1

        def major_check(num):
            count = 0
            total = len(nums) / 2

            for ele in nums:
                if ele == num:
                    count += 1

            return count > total

        major_check(major)
        return major