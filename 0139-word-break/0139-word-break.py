class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # memoization
        memo = {}

        def dfs(start_index):
            if start_index == len(s):
                return True
            if start_index in memo:
                return memo[start_index]

            ans = False
            for word in wordDict:
                if s[start_index:].startswith(word):
                    #ans= True
                    if dfs(start_index+len(word)):
                        ans = True
                        break
            memo[start_index]=ans
            return ans
        return dfs(0)        