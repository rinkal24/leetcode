class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ctr_nums = Counter(nums)
        prev = -1
        diff = math.inf
        d_num_ind = {}
        
        for i in nums:
            if ctr_nums[i] > 1:
                d_num_ind[i] = -1
                
        for ind, val in enumerate(nums):
            if val in d_num_ind:
                if d_num_ind[val] >= 0:
                    diff = min(diff, ind - d_num_ind[val])
                if diff <= k :
                    return True
                d_num_ind[val] = ind
                
        return False