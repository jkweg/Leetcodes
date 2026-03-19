# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        s = []
        res = []

        while root or s:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            res.append(root.val)

            root = root.right

        return res