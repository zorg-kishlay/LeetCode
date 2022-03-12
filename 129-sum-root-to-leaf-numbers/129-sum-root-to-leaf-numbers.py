# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,sum_val=0):
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 10*sum_val+node.val # for leaf node we just add current val to ones place of total sum
            
            return dfs(node.left,10*sum_val+node.val) + dfs(node.right,10*sum_val+node.val)
        
        return dfs(root)
        