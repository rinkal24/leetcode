class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftptr = 0
        rightptr = len(numbers) - 1
        
        while(leftptr < rightptr):
            if numbers[leftptr] + numbers[rightptr] == target:
                return [leftptr + 1, rightptr + 1]
            elif numbers[leftptr] + numbers[rightptr] > target:
                rightptr -= 1
            else:
                leftptr += 1