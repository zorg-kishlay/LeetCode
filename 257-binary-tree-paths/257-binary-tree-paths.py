# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []
        
        def roottoleaf(node,slate):
            
            slate.append(str(node.val))
            
            if not node.left and not node.right:
                result.append("->".join(slate))
                slate.pop()
                return
            
            if node.left:
                roottoleaf(node.left,slate)
            
            if node.right:
                roottoleaf(node.right,slate)
            
            slate.pop()
        
        
        roottoleaf(root,[])
        return result