# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(N)
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        # base case where we need None
        if root1 is None and root2 is None:
            return None
        
        value1 = root1.val if root1 else 0 # basically helps us at None children adding 0 has no value
        value2 = root2.val if root2 else 0
        result = TreeNode(value1+value2)
        
        result.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None)
        result.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None)
        
        return result