# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        if not root:
            return []
        
        queue= []
        queue.append(root)
        while queue:
            max_value=float("-inf")
            count = len(queue)
            
            while count>0:
                count-=1
                node=queue.pop(0)
                max_value = max(node.val,max_value)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(max_value)
        
        return result
            
        