class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0){
            return false;
        }

        long long temp=0,a=x,mid;
        while(x!=0){
            mid=x%10;
            temp=temp*10+mid;
            x/=10;
        }
        if ((a^temp)==0){
            return true;
        }
        return false;
    }
};