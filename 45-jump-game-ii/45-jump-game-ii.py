class Solution:
    def jump(self, array) -> int:

        if len(array) == 1:
            return 0

        jumps = 0
        max_reach = array[0]
        steps = array[0]
        for i in range(1, len(array) - 1):
            max_reach = max(max_reach, array[i] + i)
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = max_reach - i

        return jumps + 1
            
      #  jumps = [float("inf") for i in range(len(array))]
#         jumps[0] = 0

#         for i in range(1,len(array)):
#             for j in range(0,i):
#                 if array[j]+j>=i:
#                     jumps[i] = min(jumps[i],jumps[j]+1)

#         return jumps[-1]