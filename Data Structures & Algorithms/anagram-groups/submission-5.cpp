class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> grouping;

        for (string &str: strs){
            map<char, int> freq;
            for (char &c: str){
                freq[c]++; 
            }
            grouping[freq].push_back(str);
        }

        vector<vector<string>> res;

        for (auto [k,v] : grouping){
            res.push_back(v);
        }

        return res;
    }
};
