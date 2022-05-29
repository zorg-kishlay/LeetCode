# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        if not root:
            return result
        
        def helper(node,target,slate):
            
            # we will need to append root node to the slate
            slate.append(node.val)
            
            # leaf node when val is equal to target we append to the result
            if not node.left and not node.right:
                if node.val==target:
                    result.append(slate[:])
                
                # if leaf node doesn't add upto the target we need to pop it out
                # of slate to go check for next leaf
                slate.pop()
                return
            
            if node.left:
                helper(node.left,target-node.val,slate)
            
            if node.right:
                helper(node.right,target-node.val,slate)
            
            slate.pop() # this is to pop current elments(not leaf nodes) if they do not add up to sum
        
        helper(root,targetSum,[])
        return result
    
    #Space and Time :- O(NlogN)
    # worst case for this issue will be a complete binary tree
        