class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        ans = []
        for i in nums1:
            if i in nums2 and i not in ans:
                ans.append(i)
        return ans
        
        