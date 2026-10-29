/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    unordered_map<int, int> inorder_map;
    int pre_idx = 0;

    TreeNode *returnNode(vector<int>& preorder, int l, int r) {
        if (l > r) return nullptr;

        int root_val = preorder[pre_idx++];
        TreeNode *root = new TreeNode(root_val);
        int mid = inorder_map[root_val];

        root->left = returnNode(preorder, l, mid - 1);
        root->right = returnNode(preorder, mid + 1, r);

        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inorder_map[inorder[i]] = i;
        }

        return returnNode(preorder, 0, inorder.size() - 1);
    }
};
