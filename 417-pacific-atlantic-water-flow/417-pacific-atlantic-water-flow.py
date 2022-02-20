# O(NM) time
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we will traverse from 1 st row to pacific
        # and last column to atlantic and maintain sets
        # for each and then find all common elements
        rows, columns = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        result = []

        def dfs(row, column, ocean, prev_height):
            # since we are traversing from bottom up we are allowed only to
            # traverse to greater or equal heights
            if (row,
                column) in ocean or row < 0 or column < 0 or row == rows or column == columns or \
                    heights[row][column] < prev_height:
                return
            ocean.add((row, column))
            dfs(row + 1, column, ocean, heights[row][column])
            dfs(row - 1, column, ocean, heights[row][column])
            dfs(row, column + 1, ocean, heights[row][column])
            dfs(row, column - 1, ocean, heights[row][column])

        # for pacific first row and all columns

        for c in range(columns):
            # we pass heights[0][c] as prev_height as we know for equal heights
            # flow is possible
            dfs(0, c, pacific, heights[0][c])

            # for last row and atlantic ocean
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        # for the bottom rows
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, columns - 1, atlantic, heights[r][columns - 1])

        # once we are done we only need the common elements in both
        # pacific and atlantic sets as they will be the ones that have access
        # to atlantic and pacific oceans

        for r in range(rows):
            for c in range(columns):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result