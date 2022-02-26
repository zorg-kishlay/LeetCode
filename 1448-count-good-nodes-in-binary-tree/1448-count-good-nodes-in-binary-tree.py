# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # we will traverse in pre order and
        # pass max value so far as well
        # if current val>= max val then increase 
        # count of
        
        def pre(root, max_val):
            
            if not root:
                return 0
            
            result = 1 if root.val>=max_val else 0
            max_val = max(max_val, root.val)
            result += pre(root.left,max_val)
            result += pre(root.right,max_val)
            
            return result
        
        
        return pre(root, -float("inf"))
        