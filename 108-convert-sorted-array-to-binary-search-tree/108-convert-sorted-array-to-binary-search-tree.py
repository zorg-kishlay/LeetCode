# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def traverse(start,end):
            if start>end:
                return None
            
            mid = (end+start)//2
            root = TreeNode(nums[mid])
            root.left =  traverse(start,mid-1)
            root.right = traverse(mid+1,end)
            
            return root
        
        return traverse(0,len(nums)-1)