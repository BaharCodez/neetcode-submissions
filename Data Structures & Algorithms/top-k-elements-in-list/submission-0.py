class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        items = frequency.items()

        sorted_items = sorted(items, key =lambda x:x[1])

        top_k=sorted(sorted_items[-k:]) #reverse it

        return [x[0] for x in top_k]
