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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() == 0 || inorder.size() == 0) return NULL;
        TreeNode *root = new TreeNode(preorder[0]);

        auto pivot = find(inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        

        vector<int> inLeft(inorder.begin(), inorder.begin() + pivot);          
        vector<int> inRight(inorder.begin() + pivot + 1, inorder.end());                        
        cerr << "Try" << endl;
        vector<int> preLeft(preorder.begin() + 1, preorder.begin() + 1 + pivot);
        vector<int> preRight(preorder.begin() + pivot + 1, preorder.end());
        
        cerr << "preLeft ";
        for (int v : preLeft)
            cerr << v << ", ";
        cerr << endl;

        cerr << "preRight ";
        for (int v : preRight)
            cerr << v << ", ";
        cerr << endl;

        cerr << "inLeft ";
        for (int v : inLeft)
            cerr << v << ", ";
        cerr << endl;

        cerr << "inRight ";
        for (int v : inRight)
            cerr << v << ", ";
        cerr << endl;

        root->left = buildTree(preLeft, inLeft);
        root->right = buildTree(preRight, inRight);

        return root;
    }
};
