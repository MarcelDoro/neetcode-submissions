# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return "N"

        left_serialize = self.serialize(root.left)
        right_serialize = self.serialize(root.right)

        return f"{root.val},{left_serialize},{right_serialize}"
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(',')
        i = 0

        def dfs():
            nonlocal i 
            
            if data_list[i] == "N":
                i += 1
                return None

            node = TreeNode(int(data_list[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

