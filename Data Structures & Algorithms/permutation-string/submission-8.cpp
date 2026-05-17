class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()){
            return false;
        }

        map<int, int> freq1;
        map<int, int> freq2;
        int l = 0, r = 0;
        for ( ; r < s1.size(); r++){
            freq1[s1[r]] += 1;
            freq2[s2[r]] += 1;
        }
        
        while (r < s2.size()){
            if (freq1 == freq2) return true;
            freq2[s2[l]] -= 1;
            if (freq2[s2[l]] == 0) freq2.erase(s2[l]);
            l++;
            freq2[s2[r]] += 1;
            r++;
        }

        return freq1 == freq2;
    }
};
