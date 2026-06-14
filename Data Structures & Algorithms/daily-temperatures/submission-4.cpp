class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result (temperatures.size());
        stack<int> st; // monotonic increasing
        for (int i = temperatures.size() - 1; i >= 0; i--){
            // while current is >  stack, keep popping since itll be a closer "greater" for future indices
            while (!st.empty() && temperatures[i] >= temperatures[st.top()]) {
                st.pop();
            }

            if (st.empty()) {
                result[i] = 0; // none satisified
            }   
            else {
                result[i] = st.top() - i; // smaller than stak top
            }
            st.push(i); // always push bc even if its "small" it can > a future index

            
        }  
        return result;
    }
};
