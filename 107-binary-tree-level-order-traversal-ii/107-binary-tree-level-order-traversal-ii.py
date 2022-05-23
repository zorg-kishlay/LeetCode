# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Time and Space:- O(N)
        
        # same template just reverse the orders
        
        if not root:
            return []
        
        result = []
        queue = []
        
        queue.append(root)
        while queue:
            count = len(queue)
            level = []
            
            while count>0:
                count-=1
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            
            result.append(level)
        
        return reversed(result)
        