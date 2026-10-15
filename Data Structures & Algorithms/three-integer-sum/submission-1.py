class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for ind, num in enumerate(nums):
            if num > 0:
                break
            if ind > 0 and num == nums[ind-1]:
                continue
            left, right = ind+1, len(nums)-1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.add(tuple([num, nums[left], nums[right]]))
                    left += 1
                    right -= 1
        return [res for res in result]