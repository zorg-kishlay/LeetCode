<h2>1277. Count Square Submatrices with All Ones</h2><h3>Medium</h3><hr><div><p>Given a <code>m * n</code> matrix of ones and zeros, return how many <strong>square</strong> submatrices have all ones.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
There are <strong>10</strong> squares of side 1.
There are <strong>4</strong> squares of side 2.
There is  <strong>1</strong> square of side 3.
Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
There are <b>6</b> squares of side 1.  
There is <strong>1</strong> square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 300</code></li>
	<li><code>1 &lt;= arr[0].length&nbsp;&lt;= 300</code></li>
	<li><code>0 &lt;= arr[i][j] &lt;= 1</code></li>
</ul>
</div>

<h2> Solution </h2>
<p>
class Solution {
    public int countSquares(int[][] matrix) {
        
        // create a dp matrix with same size
        int dp[][]=new int[matrix.length][matrix[0].length];
        int count=0;
        //Strategy:- solve for largest square matrix and then add all numbers since each place will already have had accounted for itself.
        
        // since we are looking for squares the smallest problem is the last box of the matrix.
        for(int i=dp.length-1;i>=0;i--){
            for(int j=dp[0].length-1;j>=0;j--){
                
                //for all non-middle elements the largest 1 square matrix will be its value only.Since making a sqaure matrix would be outside the size range.
                if(j==dp[0].length-1 && i==dp.length-1){
                    dp[i][j]=matrix[i][j];
                }
                else if(j==dp[0].length-1){
                    dp[i][j]=matrix[i][j];
                }
                else if(i==dp.length-1){
                    dp[i][j]=matrix[i][j];
                }
                // for middle elements if value is 0 largest submatrix of 1 is will be 0
                else{
                    if(matrix[i][j]==0)
                        dp[i][j]=0;
                    else{
                //Else largets will be minm of all its sides (left,bottom and diagonal)+1
                    int minm=Math.min(dp[i][j+1],dp[i+1][j]);
                    dp[i][j]=Math.min(minm,dp[i+1][j+1])+1;
                    }
                }
            }
        }
        // after this the dp matrix would look like
/*. 0  3. 2. 1
    1. 2. 2. 1
    0. 1. 1. 1
    */
        
            for(int i=dp.length-1;i>=0;i--){
            for(int j=dp[0].length-1;j>=0;j--){
                if(dp[i][j]!=0)
                    count=count+dp[i][j];
        
    
            }
            }
        
        return count;        
}
}
</p>
