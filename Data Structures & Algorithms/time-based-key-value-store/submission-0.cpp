class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> m;
public:

    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        m[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        auto& values = m[key];
        int l = 0, r = values.size();
        string result = "";

        while (l < r){
            int mid = l + (r-l) / 2;
            if (timestamp >= values[mid].first){
                l = mid + 1;
                result = values[mid].second;
            }
            else {
                r = mid;
            }
        }
        return result;
    }
};
