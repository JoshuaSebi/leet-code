class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        reverse(arr.begin(),arr.end());
        int maxv=arr[0];
        for (int i=1;i<arr.size();i++){
            int preval=maxv;
            if (arr[i]>=maxv){
                maxv=arr[i];
            }
            arr[i]=preval;
        }
        arr[0]=-1;
        reverse(arr.begin(),arr.end());
        return arr;
    }
};