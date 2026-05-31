class Solution {
public:
    int characterReplacement(string s, int k) {
        map<char, int> freq;
        int l = 0, r = 0, maxF = 0, res = 0;
        while (r < s.size()){
            freq[s[r]] += 1;
            maxF = max(maxF, freq[s[r]]);
            int windowSize = r - l + 1;
            if (windowSize - maxF > k){
                freq[s[l]]--;
                l++;
                windowSize--;
            }
            res = max(res, windowSize);
            r++;
        }
        return res;
    }

};
