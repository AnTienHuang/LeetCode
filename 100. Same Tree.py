# 100. Same Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return True if not p and not q else False
        
        p_path = [p.val]
        q_path = [q.val]

        def dfs(root, depth, path):
            if not root:
                return
            
            if root.left:
                depth += 1
                path.append(f"l{depth}{root.left.val}")
                dfs(root.left, depth, path)
                depth -= 1
            
            if root.right:
                depth += 1
                path.append(f"r{depth}{root.right.val}")
                dfs(root.right, depth, path)
                depth -= 1

        dfs(p, 0, p_path)
        dfs(q, 0, q_path)

        return p_path == q_path

            