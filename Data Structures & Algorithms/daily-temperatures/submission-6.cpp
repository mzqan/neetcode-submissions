class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> res (n, 0); // size, default
        for (int i = n - 2; i >= 0; i--){
            int j = i + 1;

            // if next idx is smaller, finds ITS answer which could also be ours
            while (j < n && temperatures[j] <= temperatures[i]){
                if ( res[j] == 0 ){ // no greater
                    j = n; // invalidate j idx => i will stay 0
                    break;
                }
                j += res[j]; // jump to j's answer which we'll check if we can reuse
            }

            if ( j < n ){   // if j idx is valid,aka we got ans
                res[i] = j - i;
            }
        }  
        return res;
    }
};
