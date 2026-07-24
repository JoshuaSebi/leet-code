class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int f=k%(nums.begin()-nums.end());
        reverse(nums.begin(),nums.end());
        reverse(nums.begin(),nums.begin()+f);
        reverse(nums.begin()+f,nums.end());
    }
};