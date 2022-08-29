# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return root
        
        level =0
        maxSum = float("-inf")
        minLevel = 0
        
        q =collections.deque([root])
        
        while len(q)>0:
            numNodes = len(q)
            total = 0
            level+=1
            
            while numNodes>0:
                numNodes-=1
                
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
                total+=node.val
            
            if total>maxSum:
                maxSum = total
                minLevel=level
            
        return minLevel
                
        