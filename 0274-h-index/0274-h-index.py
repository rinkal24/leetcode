class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = -1
        print(citations)
        N = len(citations)
        
        i = 0
        while i < N and citations[N - 1 - i] > i:
            print(i, citations[N - 1 - i])
            i += 1
            
        return i