class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        built_dict = {target - num: [] for num in nums}

        for i in range(len(nums)):
            built_dict[target - nums[i]].append((nums[i], i))

        print(built_dict)

        for i in range(len(nums)):
            if nums[i] in built_dict:
                for tup in built_dict[nums[i]]:
                    if i != tup[1]:
                        return [i, tup[1]]