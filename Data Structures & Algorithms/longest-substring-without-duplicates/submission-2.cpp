class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = 0;
        int res = 0;
        set<int> seen;
        while (r < s.size()){
            if (seen.contains(s[r])){
                seen.clear();
                l++;
                r = l;
            }
            else { 
                seen.insert(s[r]);
                res = max(res, r - l + 1);
                r++;
            }
        }
        return res;
    }
};
