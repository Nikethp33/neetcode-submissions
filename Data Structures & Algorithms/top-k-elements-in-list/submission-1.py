class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n,0) + 1

        sorted_count = sorted (count.items(), key=lambda x: x[1], reverse=True)

        ans = [item[0] for item in sorted_count[:k]]

        return ans