import heapq

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        #arr = []
       # heapq.heapify(arr)

       # for key, val in counter.items():
       #     heapq.heappush(A, key)

        heap = []
        for key, val in counter.items():
        # Push a tuple (priority, item)
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [item[1] for item in heap]

        return result

