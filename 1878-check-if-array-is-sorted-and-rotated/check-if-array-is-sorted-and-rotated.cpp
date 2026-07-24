class Solution {
public:
    bool check(vector<int>& nums) {
        int l=nums.size();
        int c=0;
        for (int i=0;i<l;i++){
            if (nums[i]>nums[(i+1)%l]){
                c++;
            }
        }
        if (c<=1){
            return true;
        }
        return false;
    }
};