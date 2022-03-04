# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        # first value of pre is root
        
        root = TreeNode(preorder[0])
        
        in_index = inorder.index(root.val) # find index of root in inorder list
        
        # this helps us in deciding the no of elements in left and right of the current root
        
        #left sublist
        root.left = self.buildTree(preorder[1:in_index+1],inorder[:in_index])
        # right sublist
        root.right = self.buildTree(preorder[in_index+1:],inorder[in_index+1:])
        
        
        return root