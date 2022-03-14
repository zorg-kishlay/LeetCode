# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        # O(N) : skewed tree
        # O(h) : h- height of tree (avg) worst O(N)
        
        # base case if root is none we return none
        
        if not root: # handles all cases where we remove the subtree
            return root
        
        if root.val>high: # if the current value is greater than high that means all values
            # to the right of current would also be greater than high
            return self.trimBST(root.left,low,high) # so we just need to check for the left subtree
        
        if root.val<low:
            return self.trimBST(root.right,low,high)
        
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        
        return root
        