class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> s;
        vector<int> res;
     
        for (int i = 0; i < nums.size(); i++){
            if (!s.empty() && s.front() == i - k) {
                s.pop_front();
            }

            while (!s.empty() && nums[i] > nums[s.back()]){
                s.pop_back();
            }

            s.push_back(i);

            if (i >= k - 1) {
                res.push_back(nums[s.front()]);
            }
        }
        return res;
    }
};
