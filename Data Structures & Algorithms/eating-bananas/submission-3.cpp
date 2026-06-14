class Solution {
public:

    int hoursTaken(vector<int>& piles, double k){
        int h = 0;
        for (int i = 0; i < piles.size(); i++){
            // # of turns to complete pile
            h += ceil(piles[i] / k);
        }
        return h;
    }


    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());
        // search space: eating rate 1              -> h = # bananas
        //               eating rate max. in a pile -> h = # piles
        int l = 1, r = *max_element(piles.begin(), piles.end());
        int res = r;

        // search space [l, r)
        while (l < r) {
            // get middle, k
            int k = l + (r-l) / 2;

            // get hours taken for k
            int t = hoursTaken(piles, k);

            // if its valid (< or lower than required)
            if (t <= h) {
                // try a smaller number next time, "better min"
                r = k;
                res = min(res, k);
            }
            else {
                l = k + 1;
            }
        }

        return res;
    }


};
