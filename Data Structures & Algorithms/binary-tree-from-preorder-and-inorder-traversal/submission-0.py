# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pidx = 0
        def build(inord):
            if not inord:
                return None

            nonlocal pidx
            n = TreeNode(preorder[pidx])
            idx = inord.index(preorder[pidx])
            pidx += 1
            n.left = build(inord[:idx])
            n.right = build(inord[idx+1:])
            return n

        return build(inorder)
