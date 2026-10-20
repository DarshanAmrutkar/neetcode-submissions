class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if height is None:
            return result
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]
        return result
