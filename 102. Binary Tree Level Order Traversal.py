# 102. Binary Tree Level Order Traversal
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
        res = []
        q = [(0, root)]

        while q:
            tmp = []
            for lv, n in q:
                if lv == len(res):
                    res.append([n.val])
                else:
                    res[lv].append(n.val)
                if n.left:
                    tmp.append((lv + 1, n.left))
                if n.right:
                    tmp.append((lv + 1, n.right))
            q = tmp

        return res