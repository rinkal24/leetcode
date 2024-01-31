class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(nums)):
            d[nums[i]] = target - nums[i]
            if d[nums[i]] in nums:
                val = nums.index(d[nums[i]])
                if val == i:
                    continue
                res.append(i)
                res.append(val)
                return res
        return res
