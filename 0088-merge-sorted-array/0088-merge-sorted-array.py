class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        comp = len(nums1) - m
        while(i != len(nums1) and j < len(nums2)):
            if(nums1[i] == 0 and len(nums1) - i == n):
                nums1[i] = nums2[j]
                i += 1
                j += 1
                n -= 1
            else:
                if(nums1[i] < nums2[j]):
                    i += 1
                    m -= 1
                elif(nums1[i] >= nums2[j]):
                    temp = nums1[i]
                    nums1[i] = nums2[j]
                    for ind in range(i + 1, len(nums1)):
                        temp2 = nums1[ind]
                        nums1[ind] = temp
                        temp = temp2
                    j += 1
                    i += 1
                    n -= 1
                    print(n)
                    print(i,j)
                    print(nums1)
                
          
        