# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isTreesSame(self, root1, root2):
        if root1.left == None and root2.left != None:
            return False
        if root1.left != None and root2.left == None:
            return False
        if root1.right == None and root2.right != None:
            return False
        if root1.right != None and root2.right == None:
            return False

        if root1.val != root2.val:
            return False

        if root1.left != None and root2.left != None:
            if self.isTreesSame(root1.left, root2.left) == False:
                return False

        if root1.right != None and root2.right != None:
            if self.isTreesSame(root1.right, root2.right) == False:
                return False

        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val:
            print("I am")
            if self.isTreesSame(root, subRoot) == True:
                return True          

        if root.left != None and self.isSubtree(root.left, subRoot) == True:
            return True
        if root.left != None and self.isSubtree(root.left, subRoot) == False:
            return False
        if root.right != None and self.isSubtree(root.right, subRoot) == True:
            return True
        if root.right != None and self.isSubtree(root.right, subRoot) == False:
            return False

        return False
            
        