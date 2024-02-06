class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        
        area = 0
        while(left_ptr <= right_ptr):
            area = max(area, min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr))
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return area