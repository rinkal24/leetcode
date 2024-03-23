class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ctr_nums = Counter(nums)
        prev = -1
        diff = math.inf
        d_num_ind = {}
        
        for i in nums:
            if ctr_nums[i] > 1 and i not in d_num_ind:
                d_num_ind[i] = -1
                
        for i in range(len(nums)):
            if ctr_nums[nums[i]] > 1:
                if d_num_ind[nums[i]] >= 0:
                    diff = min(diff, i - d_num_ind[nums[i]])
                d_num_ind[nums[i]] = i
                
        return True if diff <= k else False