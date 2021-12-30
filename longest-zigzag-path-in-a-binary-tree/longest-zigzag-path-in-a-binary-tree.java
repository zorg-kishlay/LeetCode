/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    public static class Pair{
        int forward=-1;
        int backward=-1;
        int maxLen=0;
    }
    
    public Pair longestZigZag_(TreeNode root) {
        if(root==null)
            return new Pair();
        
        Pair left=longestZigZag_(root.left);
        Pair right=longestZigZag_(root.right);
        
        Pair ans=new Pair();
        ans.maxLen = Math.max(Math.max(left.maxLen,right.maxLen),Math.max(left.backward,right.forward)+1);
        
        ans.forward=left.backward+1;
        ans.backward=right.forward+1;
        
        return ans;
        
    }
    
    
    public int longestZigZag(TreeNode root) {
        
        Pair ans=longestZigZag_(root);
        
        return ans.maxLen;
        
    }
}