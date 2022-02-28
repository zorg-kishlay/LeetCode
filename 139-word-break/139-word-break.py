class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # bottom up approach
        # we will search each word in the dictionary to check if
        # it forms our string s
        
        dp = [False] * (len(s)+1)
        
        # base case where we consider the end to be formed
        dp[-1] = True
        
        # try to solve from end of string
        
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                # to check that adding word to current index doesn’t cause overflow
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: # i.e we found a matching word
                    dp[i] = dp [i+len(word)] # our base case will help here
                
                if dp[i]:
                    break # if we have found a matching word then we don’t need to check for other words
                    # in the dict. leet will be equal to leet only not word
        
        # try running if confused
        return dp[0]
                