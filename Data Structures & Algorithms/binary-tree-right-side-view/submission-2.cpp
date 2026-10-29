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
    int height(TreeNode *root) {
        if (root == NULL) return 0;
        return 1 + max(height(root->left), height(root->right));
    }

    int rightMost(TreeNode *root, int lvl) {
        int currentLvl = 0;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();
            TreeNode *node;
            
            for (int i = 0; i < size; i++) {
                node = q.front();
                q.pop();

                if (node->left != NULL) q.push(node->left);
                if (node->right != NULL) q.push(node->right);                                
            }

            if (currentLvl == lvl) return node->val;
            currentLvl++;
        }

        return root->val;
    }

    vector<int> rightSideView(TreeNode* root) {
        vector<int> nodesVal;
        if (root == NULL) return nodesVal;
        int h = height(root);        

        for (int i = 0; i < h; i++) {
            nodesVal.push_back(rightMost(root, i));
        }

        return nodesVal;
    }
};
