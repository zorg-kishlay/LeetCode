# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Time:- O(ST) S-> subtree nodes and T-> root tree nodes
        
        # if subtree is None then regardless of the root it is always subtree
        if not subRoot:
            return True
        
        # here we know that subtree is not None then in that case an empty root would never be a suprtree of sub
        if not root:
            return False
        
        if self.isSameTree(root,subRoot):
            return True
        
        # if above returns false we can recursively call isSubtree on the left and right of root
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            
    
    
    def isSameTree(self,root,sub):
        if not root and not sub:
            return True
        
        if not root or not sub or root.val!=sub.val:
            return False
        
        return self.isSameTree(root.left,sub.left) and self.isSameTree(root.right,sub.right)
        