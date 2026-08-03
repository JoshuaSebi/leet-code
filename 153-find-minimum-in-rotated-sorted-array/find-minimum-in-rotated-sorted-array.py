class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        while True:
            if (nums[i]+1)>nums[(i+1)%len(nums)]:
                return nums[(i+1)%len(nums)]
            i=(i+1)%len(nums)