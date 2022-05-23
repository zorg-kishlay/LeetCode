# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Time and Space:- O(N)
        
        # same level order BFS template just that we don't need level array here we can have a variable
        # which we can keep writing over forcing it to have the last element of each level i.e right most element
        
        if root is None:
            return []
        
        queue= []
        queue.append(root)
        result = []

        while queue:
            right=None
            count = len(queue)
            
            while count>0:
                count-=1
                
                node=queue.pop(0)
                right = node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(right)
        
        return result
                    