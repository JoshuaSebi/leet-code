class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currS=nums[0]
        maxS=nums[0]
        for i in range(1,len(nums)):
            currS=max(nums[i],nums[i]+currS)
            maxS=max(currS,maxS)

        return maxS
        