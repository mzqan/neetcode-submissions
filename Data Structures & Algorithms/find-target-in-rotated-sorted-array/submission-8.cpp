class Solution {
public:
    int search(vector<int>& nums, int target) {
        // When you split a rotated sorted array in half at index m, 
        // at least one of the two halves will always be perfectly, normally sorted.
        int l = 0, r = nums.size();
        
        while (l < r){
            int m = l + (r-l)/2;
            if (nums[m] == target) {
                return m;
            }   
            //left half normally sorted
            if (nums[l] <= nums[m]){
                // target in left half
                if (nums[l] <= target && nums[m] > target){
                    r = m; // search left
                }
                else { 
                    l = m + 1; // search right
                }
            }
            // right half is normally sorted
            else {
                // target in right half
                if (nums[r-1] >= target && nums[m] < target){
                    l = m + 1;  // serach right
                }
                else {
                    r = m; // search left
                }
            }
        }

        return (l < nums.size() && nums[l] == target) ? l : -1;
    }

};
