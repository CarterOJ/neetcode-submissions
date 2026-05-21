class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for i, num in enumerate(nums):
            needed = target - num
            
            if needed in mapping:
                return [mapping[needed], i]
                
            mapping[num] = i
