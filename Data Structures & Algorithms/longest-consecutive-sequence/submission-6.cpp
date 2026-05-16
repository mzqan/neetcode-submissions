class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // set <int> seen;

        // for (int &n : nums){
        //     seen.insert(n);
        // }
        set<int> seen(nums.begin(), nums.end());


        int best = 0;
        for (int &n : nums){
            bool valid = true;
            int streak = 0;
            int i = n;
            while (valid){
                valid = seen.find(i - 1) != seen.end();
                streak++;
                i--;
            }
            best = max(best, streak);
        }
        return best;
        // map<int, int> consecutive;
        // int best = INT_MIN;

        // for (int& n: nums){
        //     if(consecutive.find(n-1) != consecutive.end()){
        //         consecutive[n] = consecutive[n-1] + 1;
        //     }
        //     else {
        //         consecutive[n] = 1;
        //     }
        //     best = max(best, consecutive[n]);
        // }
        // return best;
    }
};
