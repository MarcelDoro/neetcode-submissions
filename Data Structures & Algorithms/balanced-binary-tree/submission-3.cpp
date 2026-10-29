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

    int abs(int a) {
        if (a < 0) return -a;
        return a;
    }

    bool isBalanced(TreeNode* root) {
        if (root == NULL) return true;

        cout << "L: " << height(root->left) << endl;
        cout << "R: " <<  height(root->right) << endl;
        cout << "Dif: " <<  height(root->left) - height(root->right) << endl;
        cout << "ABS: " <<  abs(height(root->left) - height(root->right)) << endl;

        if (abs(height(root->left) - height(root->right)) > 1) {
            cout << "False" << endl;   
            return false;
        }
        
        if (isBalanced(root->left) == false) return false;
        if (isBalanced(root->right) == false) return false;

        return true;
    }
};
