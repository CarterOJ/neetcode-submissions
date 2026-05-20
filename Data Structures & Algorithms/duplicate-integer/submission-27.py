class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        poss = set(nums)
        for i in nums:
            if i in poss:
                poss.remove(i)
            else:
                return True
        return False