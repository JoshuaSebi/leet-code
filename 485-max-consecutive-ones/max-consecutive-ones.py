class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxC=0
        for i in nums:
            if i!=1:
                count=0
            else:
                count+=1
                maxC=max(maxC,count)
        return maxC