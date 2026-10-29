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
    int kthSmallest(TreeNode* root, int k) {
        vector<int> nums;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();
            TreeNode *help;

            for (int i = 0; i < size; i++) {
                help = q.front();
                q.pop();
                nums.push_back(help->val);

                if (help->left != NULL) q.push(help->left);
                if (help->right != NULL) q.push(help->right);
            }
        }

        sort(nums.begin(), nums.end());
        return nums[k - 1];
    }
};
