class Solution {
public:
    bool isPalindrome(string s) {
        string ans;
        for (int i=0; i<s.length();i++){
            if(isalnum(s[i])){
                ans+=tolower(s[i]);
            }
        }
        string rev=ans;
        reverse(ans.begin(),ans.end());
        if (rev==ans){
            return true;
        } return false;
    }
};