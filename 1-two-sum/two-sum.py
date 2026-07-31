class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track={}
        for i in range(0,len(nums)):
            k=target-nums[i]
            if k in track:
                return [track[k],i]
            track[nums[i]]=i
        return []