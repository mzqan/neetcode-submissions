class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> idxMap;

        for (int i = 0; i < nums.size(); i++){
            int t = target - nums[i];
            if (idxMap.find(t) == idxMap.end()){
                idxMap[nums[i]] = i;
            }
            else {
                return {idxMap[t], i};
            }
        }
    }
};
