class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> ref = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        stack<char> st;
        for (char c : s){
            if (ref.contains(c)){
                if (st.empty() || st.top() != ref[c]) {
                    return false;
                }
                st.pop();
            }
            else {
                st.push(c);
            }
        }
        return st.empty();
    }
};
