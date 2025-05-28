# 235. Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        
        def dfs(root, p, q):
            if not root:
                return
            
            if self.in_tree(root, p) and self.in_tree(root, q): 
                stack.append(root)

            if (p.val == root.val or 
                q.val == root.val or 
                (p.val < root.val and q.val > root.val)
            ):
                return
            if p.val < root.val:
                dfs(root.left, p, q)
            else:
                dfs(root.right, p, q)
                
        if p.val > q.val:
            p, q = q, p
        dfs(root, p, q)        
        return stack[-1]
    
    def in_tree(self, root, node):
        if not root:
            return False
        if root.val == node.val:
            return True
        return self.in_tree(root.left, node) or self.in_tree(root.right, node)