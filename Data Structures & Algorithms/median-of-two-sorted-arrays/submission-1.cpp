class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        int m = nums2.size();

        int nums[m + n] = {};
        int i = 0;
        int j = 0;
        while (i < n && j < m) {
            if (nums1[i] < nums2[j]) {
                nums[i + j] = nums1[i];
                i++;
            } else {
                nums[i + j] = nums2[j];
                j++;
            }
        }

        while (i < n) {
            nums[i + j] = nums1[i];
            i++;
        }

        while (j < m) {
            nums[i + j] = nums2[j];
            j++;
        }

        for (int k=0; k<m+n; k++) cout << nums[k] << " ";
        int s = (m + n) / 2;

        if ((m + n) % 2 == 0) return (nums[s - 1] + nums[s]) / 2.0;
        else return nums[s];
    }
};
