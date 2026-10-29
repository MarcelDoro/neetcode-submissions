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
    int maxi = 0;

    int maxDepth(TreeNode* root, int depth = 1) {
        if (root == NULL) return 0;
        if (root -> left == NULL && root -> right == NULL) return 1;

        if (root -> left != NULL) {
            depth += 1;
            if (depth > maxi) maxi = depth;
            maxDepth(root -> left, depth);
        }
        if (root -> right != NULL) {
            if (root -> left == NULL) depth += 1;
            if (depth > maxi) maxi = depth;
            maxDepth(root -> right, depth);
        }

        return maxi;
    }
};
