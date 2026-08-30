class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = dict()

        # for num in nums:
        #     if num not in freqDict:
        #         freqDict[num] = 1
        #     else:
        #         freqDict[num] +=1
        
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        numList = list(num for num in freqDict.keys())
        numList.sort(key= lambda num: freqDict[num],reverse=True)

        return numList[:k]