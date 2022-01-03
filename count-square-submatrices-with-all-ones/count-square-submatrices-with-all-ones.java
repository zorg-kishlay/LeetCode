class Solution {
    public int countSquares(int[][] matrix) {
        
        int dp[][]=new int[matrix.length][matrix[0].length];
        int count=0;
        for(int i=dp.length-1;i>=0;i--){
            for(int j=dp[0].length-1;j>=0;j--){
                
                if(j==dp[0].length-1 && i==dp.length-1){
                    dp[i][j]=matrix[i][j];
                }
                else if(j==dp[0].length-1){
                    dp[i][j]=matrix[i][j];
                }
                else if(i==dp.length-1){
                    dp[i][j]=matrix[i][j];
                }
                else{
                    if(matrix[i][j]==0)
                        dp[i][j]=0;
                    else{
                    int minm=Math.min(dp[i][j+1],dp[i+1][j]);
                    dp[i][j]=Math.min(minm,dp[i+1][j+1])+1;
                    }
                }
            }
        }
        
            for(int i=dp.length-1;i>=0;i--){
            for(int j=dp[0].length-1;j>=0;j--){
                if(dp[i][j]!=0)
                    count=count+dp[i][j];
        
    
            }
            }
        
        return count;        
}
}