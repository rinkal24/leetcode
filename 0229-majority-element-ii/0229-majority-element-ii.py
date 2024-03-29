class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = int(n/3)
        
        ctr_n = Counter(nums)
        res = []
        for i in ctr_n:
            if ctr_n[i] > limit:
                res.append(i)
        return res