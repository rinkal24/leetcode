from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctrList = Counter(nums)
        return max(ctrList, key=ctrList.get)
        