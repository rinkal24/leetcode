class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        ctr2 = Counter(nums2)
        ctr_ans = {}
        for i in nums1:
            if i in nums2 :
                if i in ans:
                    if ctr_ans[i] < ctr2[i]:
                        ans.append(i)
                        ctr_ans[i] += 1
                else:
                    ans.append(i)
                    ctr_ans[i] = 1
        return ans
                
                
                