class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty()) return "";

        map<char, int> freqT;
        for (char c : t){
            freqT[c] += 1;
        }

        map<char, int> window;
        int have = 0, need = freqT.size();
        int resLen = INT_MAX;
        pair<int, int> res = {-1, -1};
        int l = 0;
        for(int r = 0; r < s.length(); r++){
            char c = s[r];
            window[c]++;
            
            if (freqT.contains(s[r]) && freqT[c] == window[c]){
                have++;
            }
            while (have == need){
                if ((r - l + 1) < resLen){
                    resLen = r - l + 1;
                    res ={l,r};
                }

                window[s[l]]--;
                if (freqT.contains(s[l]) && window[s[l]] < freqT[s[l]]){
                    have--;
                }
                l++;
            }
        }
        return resLen == INT_MAX ? "" : s.substr(res.first, resLen);
    }
};
