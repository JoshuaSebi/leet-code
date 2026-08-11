class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum1=nums[0]
        maxSum=nums[0]
        set1=set(nums)
        for i in range(1,len(nums)):
            if nums[i]==(nums[i-1]+1):
                sum1+=nums[i]
            else:
                break
                sum1=nums[i]
            maxSum=max(maxSum,sum1)
        while maxSum in set1:
            maxSum+=1

        return maxSum