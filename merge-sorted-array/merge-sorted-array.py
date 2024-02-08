class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        rightptr = len(nums1) - 1
        
        while n > 0 and m > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                
                nums1[rightptr] = nums1[m - 1]
                nums1[m - 1] = 0
                m -= 1
                
            else:
                nums1[rightptr] = nums2[n - 1]
                n -= 1
            rightptr -= 1
        
        
        while n > 0:
            nums1[rightptr] = nums2[n - 1]
            rightptr -= 1
            n -= 1
            
        while m > 0:
            nums1[rightptr] = nums1[m - 1]
            rightptr -= 1
            m -= 1
        
          
        