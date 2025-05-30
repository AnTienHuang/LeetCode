# 230. Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = [root.val]
        q = [root]

        while q:
            node = q.pop(0)
            if node.left:
                index = vals.index(node.val)
                vals.insert(index, node.left.val)
                q.append(node.left)
            if node.right:
                index = vals.index(node.val)
                q.append(node.right)
                vals.insert(index + 1, node.right.val)

        return vals[k - 1]