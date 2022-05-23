# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # Time and Space:- O(N)
        
        # same logic and template as that of Level order we will just use a boolean flip to insert into
        # the final result to minimise the risk of wrong insertions
        
        
        if not root:
            return []
        queue = []
        result = []
        
        flip = False
        
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
            
            if flip:
                result.append(reversed(level))
                
            else:
                result.append(level)
            flip=not flip
        
        return result
            
        