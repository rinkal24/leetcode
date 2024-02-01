class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader = 1
        writer = 0
        
        writectr = 1
        while reader < len(nums):
            if nums[reader] == nums[writer] :
                writectr += 1
                if writectr <= 2:
                    writer += 1
                    nums[writer] = nums[reader]
                    reader += 1
                else:
                    reader += 1
            else:
                writectr = 1
                writer += 1
                nums[writer] = nums[reader]
                reader += 1
        return writer + 1