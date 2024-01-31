class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ind = len(nums) - 1
        nn = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val and nn == 0:
                ind -= 1
                dummy = nums[i - 1]
            elif nn > 0 and nums[i] == val:
                nums[i] = nums[ind]
                ind -= 1
            else:
                nn += 1
        return nn