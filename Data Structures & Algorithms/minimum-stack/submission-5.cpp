class MinStack {
public:
    stack<int> st;
    stack<int> mSt;

    MinStack() {}
    
    void push(int val) {
        st.push(val);
        if (mSt.empty() || val < mSt.top()){
            mSt.push(val);        
        }
        else {
            mSt.push(mSt.top());
        }
    }
    
    void pop() {
        mSt.pop();
        st.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return mSt.top();
    }
};
