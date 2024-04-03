class Solution:
    def reverseNums(self, neg):
        nums_len = len(neg) - 1
        ctr = 0
        print(nums_len)
        while ctr <= nums_len:
            neg[ctr], neg[nums_len] = neg[nums_len], neg[ctr]
            nums_len -= 1
            ctr += 1
        return neg
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        res = []
        pos = 0
        
        for i in nums:
            if i < 0:
                neg.append(i)
                pos += 1
            else:
                break
               
            
        neg = self.reverseNums(neg)
        ctr = 0  
        
        while pos < len(nums) or ctr < len(neg):
            
            if (ctr < len(neg) and pos >= len(nums)) or (ctr < len(neg) and pos < len(nums) and abs(neg[ctr]) < nums[pos]):
                    res.append(neg[ctr] * neg[ctr])
                    ctr += 1
            elif pos < len(nums):
                res.append(nums[pos] * nums[pos])
                pos += 1
            
        return res
            