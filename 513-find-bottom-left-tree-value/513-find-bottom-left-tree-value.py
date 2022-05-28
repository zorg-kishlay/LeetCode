# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return []
        
        queue =[]
        queue.append(root)
        result=None
        while queue:
            count = len(queue)
            left = None
            while count>0:
                count-=1
                node = queue.pop(0)
                
                left = node.val
                
                if node.right:
                    queue.append(node.right)
                
                if node.left:
                    queue.append(node.left)
            
            result =left
        
        return result
                
        