class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        # create a 2d matrix to store LCS for both strings
        lcs =[[0 for i in range(len(str1)+1)] for x in range(len(str2)+1)]
        # we know for corners lcs=0 because the lonest common subsequnce is actually empty string
        
        for i in range(1,len(str2)+1):
            for j in range(1,len(str1)+1):
                
# if the char is same that means we take the max of previous highest that would be at the diagonal and add 1 to it since we will be considering this character as its common
                if str2[i-1] == str1[j-1]:
                    lcs[i][j]=lcs[i-1][j-1]+1
                
                else:
# if character is not same that means we assign value of the max between the adjacent
                    
                    lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
        
        return lcs[-1][-1]
        
        