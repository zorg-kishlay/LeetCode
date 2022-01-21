# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.getTreeInfo(root).dia
    
    def getTreeInfo(self,tree):
        if tree is None:
            return TreeInfo(0,0)

        leftTreeInfo = self.getTreeInfo(tree.left)
        rightTreeInfo = self.getTreeInfo(tree.right)

        longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
        maxDia = max(leftTreeInfo.dia,rightTreeInfo.dia)
        currentDia = max(longestPathThroughRoot,maxDia)
        currentHeight = 1+ max(leftTreeInfo.height,rightTreeInfo.height)

        return TreeInfo(currentDia,currentHeight)

class TreeInfo:
	def __init__(self,dia,height):
		self.dia=dia
		self.height=height