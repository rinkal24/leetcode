class Solution:
    def trap(self, height: List[int]) -> int:
        left_pos, right_pos = 0, len(height) - 1
        
        left_max, right_max = 0, 0
        ans = 0
        
        while left_pos < right_pos:
            left_max = max(left_max, height[left_pos])
            right_max = max(right_max, height[right_pos])
            
            if height[left_pos] < left_max:
                ans += left_max - height[left_pos]
            
            if height[right_pos] < right_max:
                ans += right_max - height[right_pos]
            
            if height[left_pos] < height[right_pos]:
                left_pos += 1
            else:
                right_pos -= 1
                
        return ans
                
                