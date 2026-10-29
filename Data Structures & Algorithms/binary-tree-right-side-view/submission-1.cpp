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

    TreeNode *visible(TreeNode *root, int lvl) {
        int currentLvl = 0;
        queue<TreeNode*> q;
        q.push(root);

        while (q.empty() == false) {
            int size = q.size();
            TreeNode *help;
            TreeNode *rightMost;

            for (int i = 0; i < size; i++) {
                help = q.front();
                q.pop();

                rightMost = help;

                if (help->left != NULL) q.push(help->left);
                if (help->right != NULL) q.push(help->right);
            }
            
            if (currentLvl == lvl) return rightMost;
            currentLvl++;
        }

        return root;
    }

    vector<int> nodes;

    vector<int> rightSideView(TreeNode* root) {
        int h = height(root);

        for (int i = 0; i < h; i++) {
            nodes.push_back(visible(root, i)->val);
        }

        return nodes;
    }
};
