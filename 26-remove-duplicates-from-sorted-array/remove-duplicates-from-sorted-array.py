class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sett=set()
        for i in range(len(nums)-1,-1,-1):
            if nums[i] not in sett:
                sett.add(nums[i])
            else:
                del nums[i]
        return len(nums)