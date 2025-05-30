# 98. Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root, min_val, max_val):
            if not root:
                return
            
            if root.val <= min_val or root.val >= max_val:
                self.res = False
                return
            
            dfs(root.left, min_val, root.val)
            dfs(root.right, root.val, max_val)

        dfs(root, float("-inf"), float("inf"))
        return self.res