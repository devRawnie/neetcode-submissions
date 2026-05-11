# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None

        def lca(node):
            if not node:
                return None

            if p.val < node.val and q.val < node.val:
                return lca(node.left)

            if p.val > node.val and q.val > node.val:
                return lca(node.right)

            return node

        return lca(root)
