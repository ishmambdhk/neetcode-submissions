import collections
import heapq
from typing import Counter, List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        cntToVals = collections.defaultdict(list)

        # 1. Fixed: counter.items()
        for val, cnt in counter.items():
            cntToVals[cnt].append(val)

        # 2. Negate counts for Max-Heap
        cnts = [-cnt for cnt in cntToVals.keys()]
        heapq.heapify(cnts)

        res = []
        for i in range(len(cnts)):
            # 3. Fixed syntax: -heapq.heappop(cnts)
            next_cnt = -heapq.heappop(cnts)
            for num in cntToVals[next_cnt]:
                res.append(num)
                if len(res) == k:
                    return res

        return res