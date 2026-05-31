class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (const string& t : tokens){
            if (t == "+"){
                int l = st.top();
                st.pop();
                int r = st.top();
                st.pop();
                st.push(r + l);
            }
            else if (t == "-"){
                int l = st.top();
                st.pop();
                int r = st.top();
                st.pop();
                st.push(r - l);
            }
            else if (t == "*"){
                int l = st.top();
                st.pop();
                int r = st.top();
                st.pop();
                st.push(r * l);
            }
            else if (t == "/"){
                int l = st.top();
                st.pop();
                int r = st.top();
                st.pop();
                st.push(r / l);
            }
            else{
                st.push(stoi(t));
            }
        }
        return st.top();
    }
};
