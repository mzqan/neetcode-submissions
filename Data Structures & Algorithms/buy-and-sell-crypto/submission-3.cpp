class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int l = 0, r = 1;
        while (r < prices.size()){
            int curr = prices[r] - prices[l];
            res = max(curr, res);
            if (prices[r] < prices[l]){
                l = r;
            }
            r++;
        }   
        return res; 
    }
};
