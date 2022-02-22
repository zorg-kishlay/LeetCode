class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # O(ElogV)
        # worst case E = V2 where we will pushing each edge to heap
        # so heap operation would be logV2 and sicne we do it for all edges
        # O(ElongV2)== O(2ElogV)== O(ElogV)

        edges = collections.defaultdict(list)

        # creating adjacency list
        for vertex1, vertex2, weight in times:
            print(vertex1, vertex2, weight)
            edges[vertex1].append((weight, vertex2))

        # creating a min heap with value 0 and starting vertex k

        min_heap = [(0, k)]
        visited = set()
        result = 0

        while min_heap and len(visited)<n:
            weight, vertex = heapq.heappop(min_heap)
            visited.add(vertex)
            result = max(result, weight)

            # so basically check for neighbours
            for weight2, neighbour in edges[vertex]:
                if neighbour not in visited:
                    # pushing weight2+weight because we want to keep track of
                    # total distance to reach the node
                    heapq.heappush(min_heap, (weight2 + weight, neighbour))

        return result if len(visited) == n else -1