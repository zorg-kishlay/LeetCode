class Solution:
    def smallestNumber(self, num: int) -> int:

        # if number is 0 then minm is also 0
        if num == 0:
            return 0

        # for positive numbers
        if num > 0:
            result = "".join(sorted(str(num)))

            # if we have preceding 0s
            if result[0] == "0":
                length = len(result)
                for i in range(length):
                    # find the first non-zero number - append all 0s after that
                    # and all later elements after that
                    # This works because we know that result array is already sorted
                    if result[i] != "0":
                        return int(result[i] + result[:i] + result[i + 1:])
            return int(result)
        if num < 0:
            # for negative numbers - will come before all numbers so we
            # need to remove it before converting it to int
            result = "".join(sorted(str(num)[1:], reverse=True))
            return -int(result)