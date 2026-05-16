class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() -1;

        while (l < r){
            int look = target - numbers[l];
            while(numbers[r-1] >= look && l <= r) r--;
            if (numbers[r] == look){
                return {l+1,r+1};
            }
            l++;


            // int curSum = numbers[l] + numbers[r];

            // if (curSum > target) {
            //     r--;
            // } else if (curSum < target) {
            //     l++;
            // } else {
            //     return { l + 1, r + 1 };
            // }
        }
    }
};
