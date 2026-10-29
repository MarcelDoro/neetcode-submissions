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
    vector<vector<int>> nodes;
    int level = 0;
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) return nodes;
        
        if (nodes.size() == level) nodes.push_back({});
        if (root != NULL) nodes[level].push_back(root->val);

        if (root->left != NULL) {
            level++;
            levelOrder(root->left);
        }

        if(root->right != NULL) {
            level++;
            levelOrder(root->right);
        }

        level--;

        return nodes;
    }
};
