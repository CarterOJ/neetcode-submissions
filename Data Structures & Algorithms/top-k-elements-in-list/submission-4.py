class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {num: 0 for num in nums}
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            count[num] += 1
            
        for num in count:
            buckets[count[num]].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            if len(buckets[i]) > 0:
                for j in range(len(buckets[i]) - 1, -1, -1):
                    if len(result) < k:
                        result.append(buckets[i][j])
                
        return result