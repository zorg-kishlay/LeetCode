from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return root
            
        result = []
        flag = True

        queue = deque([root])

        while len(queue)!=0:
            count = len(queue)
            temp = []

            for _ in range(count):
                node = queue.popleft()
                temp.append(node.val)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)
            if flag:
                result.append(temp)
            else:
                result.append(temp[::-1])
            
            flag = not flag
        
        return result

        