class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # O(N2) time
        
        # we take each element and try to find how long(if possible) of a palindorme
        # is possible with the element in the center
        # one other wat would be to take each element and find its subsequences O(N2) and
        # then check if its palindrome O(N) so total would be O(N3)
        
        
        result = ""
        longest_length = 0 
        
        for idx in range(len(s)):
            
            # for odd length
            left= right= idx
            # take idx at center and check
            while left >=0 and right < len(s) and s[left]==s[right]:
                current = right-left+1
                if current > longest_length:
                    result = s[left:right+1]
                    longest_length = current
                
                left -=1
                right +=1
            
            # for even length
            left, right= idx,idx+1
            # take idx at center and check
            while left >=0 and right < len(s) and s[left]==s[right]:
                current = right-left+1
                if current > longest_length:
                    result = s[left:right+1]
                    longest_length = current
                
                left -=1
                right +=1
        
        return result