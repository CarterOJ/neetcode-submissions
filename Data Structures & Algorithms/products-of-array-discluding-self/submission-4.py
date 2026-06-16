class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        length = len(nums)

        for i in range(length):
            if i == 0:
                continue
            elif i == 1:
                prefix[i] *= nums[i - 1]
            else:
                prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(length - 1, -1, -1): 
            if i == length - 1:
                continue   
            elif i == length - 2:
                suffix[i] *= nums[i + 1]
            else:
                suffix[i] = nums[i + 1] * suffix[i + 1]

        print(prefix)
        print(suffix)

        return [prefix[i] * suffix[i] for i in range(length)]
