


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def tr(self, n, d, x, y):
        if n.val == x:
            self.levelX = d
            return

        if n.val == y:
            self.levelY = d
            return

        if n.left != None:
            self.tr(n.left, d + 1, x, y)

        if n.right != None:
            self.tr(n.right, d + 1, x, y)

        if self.levelX != -1 and self.parentX == -1:
            self.parentX = n.val
        if self.levelY != -1 and self.parentY == -1:
            self.parentY = n.val

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.levelX = -1
        self.parentX = -1
        self.levelY = -1
        self.parentY = -1
        self.tr(root, 0, x, y)

        return self.levelX == self.levelY and self.parentX != self.parentY
        	