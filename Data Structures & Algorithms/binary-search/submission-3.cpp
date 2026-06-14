class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();
        // search space is [l, r)
        while (l < r){
            int m = l + (r - l) / 2;
            if (nums[m] >= target){
                r = m;
            }
            else {
                l = m + 1;
            }
        }
        // left is either the answer or invalid
        return (l < nums.size() && nums[l] == target) ? l : -1;
    }
};
