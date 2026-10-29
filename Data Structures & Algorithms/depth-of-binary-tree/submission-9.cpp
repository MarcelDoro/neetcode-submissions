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
    int maxDepth(TreeNode* root) {
        if (root == NULL) return 0;
        
        stack <pair<TreeNode*, int>> nodes;
        nodes.push({root, 1});

        int maxi = 0;
        int depth = 0;
        TreeNode *help;
        while (nodes.empty() == false){
            auto [help, depth] = nodes.top();
            nodes.pop();

            if (depth > maxi) maxi = depth;

            if (help -> right != NULL){
                nodes.push({help -> right, depth + 1});
            }
            if (help -> left != NULL){
                nodes.push({help -> left, depth + 1});
            }
        }

        return maxi;
    }
};
