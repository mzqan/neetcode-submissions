class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for (int &n: nums){
            freq[n]++;
        }
        priority_queue<pair<int, int>> pq;
        for (auto &[k, v] : freq){
            pq.push({v, k});
        }
        vector<int> res;
        for (int i = 0; i < k; i++){
            auto el = pq.top();
            pq.pop();
            res.push_back(el.second);
        }
        return res;
    }
};
