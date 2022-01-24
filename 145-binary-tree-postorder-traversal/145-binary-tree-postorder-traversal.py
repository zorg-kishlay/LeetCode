# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post(self,node,li):
        if node.left is not None:
            self.post(node.left,li)
        if node.right is not None:
            self.post(node.right,li)
        li.append(node.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
               
        if root is None:
            return []
        
        li = []
        self.post(root,li)
        return li

        