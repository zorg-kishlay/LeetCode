class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


        deadend = set(deadends)
        if "0000" in deadend:
            return -1

        queue = deque([("0000",0)])
        visited = set("0000")
        while queue:

            current,moves = queue.popleft()

            if current == target:
                return moves
            for i in range(4):
                for delta in [-1,1]:
                    new_digit = (int(current[i])+delta)%10
                    new_combo = current[:i] + str(new_digit)+ current[i+1:]

                    if new_combo not in visited and new_combo not in deadend:
                        queue.append((new_combo,moves+1))
                        visited.add(new_combo)
        return -1