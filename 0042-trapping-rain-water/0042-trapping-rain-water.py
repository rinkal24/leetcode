class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_pos = 0
        right_pos = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        
        while left_pos < right_pos:
            
            left_max = max(height[left_pos], left_max)
            right_max = max(height[right_pos], right_max)
            
            if height[left_pos] < left_max:
                ans += left_max - height[left_pos]
            
            if height[right_pos] < left_max:
                ans += right_max - height[right_pos]
                
            if height[left_pos] < height[right_pos]:
                left_pos += 1
            else:
                right_pos -= 1
        return ans