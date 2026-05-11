# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        result = []
        while q:
            tq = []
            tr = []
            for node in q:
                tr.append(node.val)
                if node.left:
                    tq.append(node.left)
                if node.right:
                    tq.append(node.right)

            result.append(tr)
            q = tq

        return result