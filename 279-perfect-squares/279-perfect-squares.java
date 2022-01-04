class Solution {
    public int numSquares(int n) {
        
        // LIS subtype
        
        int [] dp=new int[n+1];
        
        // since 0 is 0^2 and 1= 1^2
        dp[0]=0;
        dp[1]=1;
        
        for( int i=2;i<=n;i++){
            int min=Integer.MAX_VALUE;
            // since j*j can have arrray index out of bounds
            for( int j=1 ; j*j<=i;j++){
                int rem=i-j*j;
                if(dp[rem]<min)
                    min=dp[rem];
                
            }
            // 1 step when we subtract i-j*j
            dp[i]=min+1;
        }
        return dp[n];
    }
}