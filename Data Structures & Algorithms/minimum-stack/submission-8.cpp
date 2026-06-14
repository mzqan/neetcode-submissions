class MinStack {
public:
    stack<long> st; // holds difference b/w pushed value and currnt min
    long m; // curr min

    MinStack() {}
    
    void push(int val) {
        // set min to be the val if empty 
        if (st.empty()){
            st.push(0);
            m = val;
        }
        else {
            st.push(val-m);  // push diff between min/val
            if (val < m) m = val; // update min if new min (diff is negativee)
        }
    }
    
    void pop() {
        if (st.top() < 0){ // diff is negative, the poppped is the min
            m = m - st.top();  // update min
        }
        st.pop();
    }
    
    int top() {
        if (st.top() > 0){ // diff is positive, get the min
            return st.top() + m;
        } 
        return (int) m;
    }
    
    int getMin() {
        return (int)m;
    }
};
