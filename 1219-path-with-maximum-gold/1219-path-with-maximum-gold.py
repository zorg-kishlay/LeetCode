def find_max_gold(grid, i, j, row, column, visited):
    # Return zero if:-
    # 1) if indices are out of bounds
    # 2) if already visited
    # 3) if value at i,j is 0
    if i < 0 or j < 0 or i >= row or j >= column or grid[i][j] == 0 or visited[i][j]:
        return 0

    visited[i][j] = True
    left = find_max_gold(grid, i, j - 1, row, column, visited)
    right = find_max_gold(grid, i, j + 1, row, column, visited)
    up = find_max_gold(grid, i - 1, j, row, column, visited)
    down = find_max_gold(grid, i + 1, j, row, column, visited)
    visited[i][j] = False
    return max(left, right, up, down) + grid[i][j]

# time : O(M*N) space: O(M*N)
class Solution:
    def getMaximumGold(self, grid):
        if grid is None or len(grid) == 0:
            return 0

        row = len(grid)
        column = len(grid[0])
        max_gold = 0
        visited = [[False for _ in range(column)] for _ in range(row)]
        print(visited)

        for idx in range(row):
            for idxj in range(column):
                if grid[idx][idxj] > 0:
                    gold = find_max_gold(grid, idx, idxj, row, column, visited)
                    max_gold = max(gold, max_gold)
        return max_gold