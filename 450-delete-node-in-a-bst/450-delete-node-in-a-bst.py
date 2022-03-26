# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # for case where the node has no childrens then we can just return none
        if not root:
            return None
        
        # for sub cases of not having a left or a right child
        if key == root.val:
            if not root.right:
                return root.left
            
            if not root.left:
                return root.right
        
            # if we reach here it means the child has both children
            # we simply go right once and then left until last
            temp = root.right

            while temp.left:
                temp=temp.left
            root.val = temp.val
            root.right=self.deleteNode(root.right,root.val)
        
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        
        if key>root.val:
            root.right=self.deleteNode(root.right,key)
        
        return root
    
    # Time: O(h) h is height of BST
        