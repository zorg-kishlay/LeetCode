# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Python iterative O(N) time and O(H) space
        
        dummy = TreeNode()
        node = dummy
        
        stack= []
        if root:
            stack.append(root)
        
        while stack:
            current = stack.pop()
            node.right=current
            node.left=None
            node=current
            
            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)