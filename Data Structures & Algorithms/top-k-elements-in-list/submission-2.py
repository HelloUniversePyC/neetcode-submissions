from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1

        buckets = [[] for _ in range(len(nums) + 1)]
        for item,freq in counts.items():
            buckets[freq].append(item)

        output = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output




        