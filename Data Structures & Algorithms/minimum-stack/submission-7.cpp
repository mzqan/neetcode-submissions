class MinStack {
public:
    stack<long> st;
    long m;

    MinStack() {}
    
    void push(int val) {
        if (st.empty()){
            st.push(0);
            m = val;
        }
        else {
            st.push(val-m);
            if (val < m) m = val;
        }
    }
    
    void pop() {
        if (st.top() < 0){
            m = m - st.top();
        }
        st.pop();
    }
    
    int top() {
        if (st.top() > 0){
            return st.top() + m;
        }
        return (int) m;
    }
    
    int getMin() {
        return (int)m;
    }
};
