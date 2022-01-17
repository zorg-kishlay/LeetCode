# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        level =[]
        if root is None:
            return []
        queue.append(root)
        while len(queue)>0:
            count = len(queue)
            l =[]
            for i in range(count):               
                ele = queue.pop(0)
                l.append(ele.val)

                if ele.left is not None:
                    queue.append(ele.left)
                if ele.right is not None:
                    queue.append(ele.right)
                #count+=1
            level.append(l)
            
        return level
        