class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # BRUTE
        # freqDict = dict()

        # for num in nums:
        #     freqDict[num] = freqDict.get(num, 0) + 1

        # numList = list(num for num in freqDict.keys())
        # numList.sort(key= lambda num: freqDict[num],reverse=True)

        # return numList[:k]

        # better - heap
        freqDict = dict()

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        heap = []

        for num, count in freqDict.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]