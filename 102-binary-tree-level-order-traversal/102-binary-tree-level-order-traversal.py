# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Time and Space:- O(N)
        
        # template for tree BFS prog
        
        if not root:
            return []
        
        result = []
        queue = []
        
        queue.append(root)
        
        while queue:
            count = len(queue) # this is to maintain the no of elements in each level sicnce
            # queue is changing we need to maintain this only needed if answer is needed in 2D array form
            level = []
            
            while count>0:
                
                count-=1
                node = queue.pop(0)
                level.append(node.val) # adding value to this level
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result