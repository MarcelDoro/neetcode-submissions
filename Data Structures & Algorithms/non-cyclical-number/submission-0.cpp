class Solution {
public:
    bool isHappy(int n) {        
        vector<int> seen = {};

        while (n != 1) {
            int sum = 0;
            while (n > 0) {
            int dig = n % 10;
            sum += dig * dig;
            n /= 10;
            }
            n = sum; 
            if (find(seen.begin(), seen.end(), n) != seen.end())
                return false;           
            seen.push_back(n);
        }

        return true;
    }
};
