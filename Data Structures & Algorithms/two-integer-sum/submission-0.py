class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # BRUTE
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        reqNumMap = dict()
        for ind, num in enumerate(nums):
            complement = target - num

            if complement in reqNumMap:
                return [reqNumMap[complement], ind]
            else:
                reqNumMap[num] = ind
        return []