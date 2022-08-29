# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        # Level order traversal
        
        baseVal = root.val
        
        q= []
        q.append(root)
        
        while q:
            numNode = len(q)
            while numNode>0:
                numNode-=1
                node = q.pop(0)
                if node.val != baseVal:
                    return False
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        
        return True