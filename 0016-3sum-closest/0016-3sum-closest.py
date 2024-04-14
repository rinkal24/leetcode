class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        diff = math.inf
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sumVal = nums[i] + nums[lo] + nums[hi]
                if abs(target - sumVal) < abs(diff):
                    diff = target - sumVal
                if sumVal < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff