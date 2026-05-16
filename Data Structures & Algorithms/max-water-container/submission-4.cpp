class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int best = 0;
        while (l < r){
            int curr = (r - l) * min(heights[l], heights[r]);
            best = max(best, curr);
            if (heights[l] < heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return best;
    }
};