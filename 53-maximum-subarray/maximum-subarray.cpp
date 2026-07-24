class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currentSum=nums[0], maxSum=nums[0],k=nums.size();
        for(int i=1;i<k;i++){
            currentSum=max(nums[i],currentSum+nums[i]);
            maxSum=max(maxSum,currentSum);
        } 
        return maxSum;
    }
};