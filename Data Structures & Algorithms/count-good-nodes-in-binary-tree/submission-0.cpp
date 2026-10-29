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
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);    
    }

    int numGood = 0;

    int dfs(TreeNode *root, int value) {
        if (root->val >= value) numGood++;

        if (root->left != NULL) {
            dfs(root->left, max(value, root->left->val));
        }

        if (root->right != NULL) {
            dfs(root->right, max(value, root->right->val));
        }

        return numGood;
    }


};
