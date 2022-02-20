class Solution:
    def getMaxLen(self, nums):
        # tracker for ans positve and negative
        ans = pos = neg = 0
        for num in nums:
            if num > 0:
                # increase positive length if encountered a
                # negative before increase negative
                pos, neg = pos + 1, neg + 1 if neg else 0

            # when we encounter a negative number
            # we swap the pos and neg
            elif num < 0:
                pos, neg = neg + 1 if neg else 0, pos + 1

            # reset for 0
            else:
                pos = neg = 0
            ans = max(ans, pos)

        return ans
    
    
# elements  :   9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
# pos  :   1    2    3    4     0    1     7    0    1     0     1     2     5    6     5
# neg  :   0    0    0    0     5    6     2    0    0     2     3     4     3    4     7
