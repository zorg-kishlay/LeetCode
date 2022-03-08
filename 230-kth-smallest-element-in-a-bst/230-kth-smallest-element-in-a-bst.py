# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []

        def add_to_list(node):

            elements.append(node.val)
            if node.left:
                add_to_list(node.left)
            if node.right:
                add_to_list(node.right)

        add_to_list(root)
        heapq.heapify(elements)

        for i in range(k - 1):
            heapq.heappop(elements)
        return heapq.heappop(elements)
        