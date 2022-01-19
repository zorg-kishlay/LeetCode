# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pre(self,root,li):
        li.append(root.val)
        if root.left is not None:
            self.pre(root.left,li)
        if root.right is not None:
            self.pre(root.right,li)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li =[]
        if root is not None:
            self.pre(root,li)
        return li
        