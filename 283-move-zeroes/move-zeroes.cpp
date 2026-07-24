class Solution {
public:
    void swap(int& a, int& b){
        int temp=a;
        a=b;
        b=temp;
    }
    void moveZeroes(vector<int>& nums) {
        int ind=find(nums.begin(),nums.end(),0)-nums.begin();
        int k=ind;
        for (int i=ind;i<nums.size();i++){
            if(nums[i]==0){
                continue;
            }
            swap(nums[k],nums[i]);
            k++;
        }       
    }
};