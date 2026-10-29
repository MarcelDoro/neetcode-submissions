# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q == None and p == None:
            return True
        if q == None and p != None or q != None and p == None:
            return False

        if p.val != q.val:
            return False
        if p.left != None and q.left == None or p.left == None and q.left != None:
            return False
        if p.right != None and q.right == None or p.right == None and q.right != None:
            return False

        if p.left != None and q.left != None:
            if self.isSameTree(p.left, q.left) == False:
                return False
        
        if p.right != None and q.right != None:
            if self.isSameTree(p.right, q.right) == False:
                return False
        
        return True