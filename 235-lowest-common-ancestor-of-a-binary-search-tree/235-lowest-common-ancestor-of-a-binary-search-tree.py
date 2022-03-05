# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # O(logN) :- we will be visiting 1 node at each level so basically the height of the tree
       
        # basically we will try to find out where the split of the aboce 2 nodes happen
        current = root
        
        while current:
            if p.val>current.val and q.val > current.val: # implies both of them would be the right subtree
                current = current.right
            
            elif p.val<current.val and q.val < current.val: #left subtree
                current = current.left
            
            else: # covers when either of p or q has same value as current and when they are in different subtress(then obviously the LCA would be the root)
                return current
                