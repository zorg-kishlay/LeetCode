class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> \
            List[int]:

        pre_req = {c: [] for c in range(numCourses)}

        # adding pre req for each course
        for course, prereq in prerequisites:
            pre_req[course].append(prereq)

        # course has 3 states
        # visited : course visited and added to output
        # visiting: course not added to output but added to cycle
        # unvisited: course not added to output not added to cycle
        output = []
        # 2 sets for tracking visiting and visited
        visited, cycle = set(), set()

        def dfs(crs):

            # if course in cycle means that our graph has a cycle and
            # we need to terminate
            if crs in cycle:
                return False

            # if we have already visited the course no need to revisit
            if crs in visited:
                return True

            cycle.add(crs)

            for pre in pre_req[crs]:

                # cycle detected
                if not dfs(pre):
                    return False
            # since the course's path is done
            # we remove it from cycle set
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output