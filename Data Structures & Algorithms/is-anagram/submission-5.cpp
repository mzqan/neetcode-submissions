class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        map<char, int> dictS;
        map<char, int> dictT;

        for (int i = 0; i < s.size(); i++){
            dictS[s[i]] = dictS[s[i]] + 1;
            dictT[t[i]] = dictT[t[i]] + 1;
        }

        return dictS == dictT;
    }
};
