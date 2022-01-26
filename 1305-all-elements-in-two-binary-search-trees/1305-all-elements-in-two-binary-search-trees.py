# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, roots1, li):
        if not roots1:
            return
        self.inorder(roots1.left,li)
        li.append(roots1.val)
        self.inorder(roots1.right,li)

    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        result1 = []
        result2 = []
        result = []
        self.inorder(root1, result1)
        self.inorder(root2, result2)
        i = j = 0
        while i < len(result1) and j < len(result2):
            if result1[i] < result2[j]:
                result.append(result1[i])
                i += 1
            else:
                result.append(result2[j])
                j += 1
        while i < len(result1):
            result.append(result1[i])
            i += 1

        while j < len(result2):
            result.append(result2[j])
            j += 1
        return result
        