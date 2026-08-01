class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP=nums[0]
        minP=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            oldMax=maxP
            oldMin=minP

            maxP=max(nums[i],nums[i]*oldMax,nums[i]*oldMin)
            minP=min(nums[i],nums[i]*oldMax,nums[i]*oldMin)

            ans=max(ans,maxP)
        return ans
