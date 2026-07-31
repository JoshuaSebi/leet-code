class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        settesh=set()
        for i in nums:
            if i in settesh:
                return True
            settesh.add(i)
        return False