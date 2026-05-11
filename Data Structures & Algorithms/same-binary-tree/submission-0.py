# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(node):
            if not node:
                return [None]

            return [node.val] + preorder(node.left) + preorder(node.right)

        p1 = preorder(p)
        q1 = preorder(q)

        return p1 == q1
