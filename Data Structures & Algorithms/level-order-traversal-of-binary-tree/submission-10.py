# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(root: Optional[TreeNode], lvl: int):
            if root != None:
                if len(res) <= lvl:
                    res.append([])

                res[lvl].append(root.val)

                dfs(root.left, lvl+1)
                dfs(root.right, lvl+1)

        dfs(root, 0)
        return res
