class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            bitmask = bin(i)[3:]
            curr = []
            for j in range(n):
                if bitmask[j] == "1":
                    curr.append(nums[j])
            output.append(curr)
        return output