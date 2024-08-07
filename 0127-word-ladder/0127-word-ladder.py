class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord == endWord:
            return 1
        unvisited = set(wordList) # kind of like visted but with a visited we wil hit a TLE
        queue = deque([beginWord])
        #unvisited.remove(beginWord) # which means begin is visited

        def get_neighbours(word):
            result = []

            for i in range(len(word)):
                for c in ascii_letters:
                    new_word = word[:i]+c+word[i+1:]

                    if new_word in unvisited: # again maintaining visited would lead to TLE
                        result.append(new_word)
                        unvisited.remove(new_word) # again thus visited
            return result
        
        steps = 1
        while queue:
            n = len(queue)
            steps+=1
            for _ in range(n):
                word = queue.popleft()

                for neighbour in get_neighbours(word):
                    if neighbour == endWord:
                        return steps
                    
                    queue.append(neighbour)
        
        return 0

        # Time O(M+N)
        