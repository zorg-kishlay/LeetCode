class Solution:
    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        # Using DFS

        pre_dict = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            pre_dict[course].append(pre)

        visited = set()

        def dfs(crs):

            # Base 1:
            # If already in set for current course then its a loop
            # and its not possible to take the course
            if crs in visited:
                return False

            # Base 2:
            # if course has no prerequiste then possible to take
            if not pre_dict[crs]:
                return True

            visited.add(crs)

            for ele in pre_dict[crs]:
                if not dfs(ele):
                    return False

            # we are removing the current element from the set
            visited.remove(crs)

            # setting neighbours as empty as we know that
            # for this course its possible to take it
            # will be handled by base 2 reducing effort
            pre_dict[crs] = []
            return True

        # for unconnected graph
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True