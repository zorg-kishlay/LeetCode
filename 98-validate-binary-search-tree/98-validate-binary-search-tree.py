# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # we can have a DFS solution but that would be O(N^2)
        # because we have to do it for all nodes and all subtress (N worst case)
        
        
        # what we can do is have a boundary for each node for e.x we can have 
        # for left nodes we don’t care about lower limit as long as it is less than
        # root value similarly for right we don't have upper limit so for each node we just need to do
        # 2 comparisons with lower and upper thus complexity of O(2N) or O(N)
        
        def validate(node,left,right):
            if not node:
                return True # a null node is still a valid VST
            
            if not (node.val > left and node.val< right):
                return False
            
            # since every value in left has to be < parent
            return validate(node.left,left,node.val) and validate(node.right,node.val,right)
        
        return validate(root,-float("inf"),float("inf")) # root has to no restrictions
            
            
            
            
        