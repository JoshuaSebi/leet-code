class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minP=prices[0];
        int maxP=0;
        for (int i=0;i<prices.size();i++){
            minP=min(minP,prices[i]);
            maxP=max(maxP,prices[i]-minP);
        }
        return maxP;
    }
};