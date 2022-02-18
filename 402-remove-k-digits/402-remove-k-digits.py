class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k == len(num):
            return "0"
        # we'll use stack
        stack = []
        size = len(num)
        idx = 0
        while idx < size:
            # we greedily check if the current number is smaller than the top of stack
            # we replace the top of stack with the smaller number
            while len(stack) > 0 and num[idx] < stack[len(stack) - 1] and k > 0:
                stack.pop()
                k -= 1

            stack.append(num[idx])
            idx += 1

        # for num which has increasing sequence we can
        # simply remove the last k digits
        while k > 0:
            stack.pop()
            k -= 1
        while len(stack) > 1 and stack[0] == '0':
            stack.pop(0)
        return "".join(stack)