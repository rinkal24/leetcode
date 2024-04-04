class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(curr, left_count, right_count):
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            
            if left_count < n:
                curr.append("(")
                backtrack(curr, left_count + 1, right_count)
                curr.pop()
            if right_count < left_count:
                curr.append(")")
                backtrack(curr, left_count, right_count + 1)
                curr.pop()
        backtrack([], 0, 0)
        return res