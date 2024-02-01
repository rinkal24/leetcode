class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0
        reader = 0
        while reader < len(nums):
            if nums[writer] == nums[reader]:
                reader += 1
            else:
                writer += 1
                nums[writer] = nums[reader]
                reader += 1
        return writer + 1
            