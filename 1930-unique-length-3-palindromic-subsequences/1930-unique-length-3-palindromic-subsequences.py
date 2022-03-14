class Solution:
    # O(26N)
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # since the palinfromes are of length 3 that means
        # the middle character has to be different outside 2 will have to be same
        
        # given constraints the middle one can be any of 26 charcters but the other one has to be
        # same so we can have like 26^2 diff combinations (26 for middle and 26 for outside ones)
        
        # so what we can do is take each charcter and think of it as the middle charchter and check
        # for its besides characters to be same
        
        # since its subsequnce so ut doesn't need to be contagiuos
        result = set() # set of middle and outer charcter
        
        left = set() # to keep track of all unique characters to the left of the current char
        
        right = collections.Counter(s) # a dict:- basically count each character in the string s and map to its count
        
        # we will use right to keep track of characters to the right
        
        for idx in range(len(s)):
            
            # if we have s[idx] as current char that means it is not a part of right
            
            right[s[idx]] -= 1
            
            if not right[s[idx]]:
                right.pop(s[idx])
                
            for j in range(26):
                ch = chr(ord('a')+j) # basically taking all 26 characters
            
                if ch in left and ch in right: # basically covers non-contagious as well
                    result.add((s[idx],ch)) # since it is a set the duplicates are handled
            
            left.add(s[idx]) # since now it has been iterated we need to add it to the left
        
        return len(result)
        
        
        
        
        