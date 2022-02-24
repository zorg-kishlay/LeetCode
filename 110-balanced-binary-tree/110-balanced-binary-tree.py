# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Bottom up appraoch reduces repeatative work
        # O(N)
        
        def check_height_bottom_up(root):
            
            # beacuse a leaf node is always balanced
            if root is None:
                return [True,0]
            
            # get values for left and right subtress
            left, right = check_height_bottom_up(root.left), check_height_bottom_up(root.right)
            
            # check if any of the subtrees returned false then it is not balanced
            balance_factor = left[0] and right[0] and (abs(left[1]-right[1])<=1)
            
            return [balance_factor, 1+max(left[1],right[1])]
        
        return check_height_bottom_up(root)[0]
        