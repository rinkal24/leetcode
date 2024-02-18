class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        first_num = num1[::-1]
        second_num = num2[::-1]
        
        N = len(num1) + len(num2)
        ans = [0] * N
        
        
        for ind1, digit1 in enumerate(first_num):
            for ind2, digit2 in enumerate(second_num):
                num_zeroes = ind1 + ind2
                carry = ans[num_zeroes]
                new_ans = int(digit1) * int(digit2) + carry
                ans[num_zeroes] = new_ans % 10
                ans[num_zeroes + 1] += new_ans // 10
        if ans[-1] == 0:
            ans.pop()
            
        return ''.join(str(digit) for digit in reversed(ans))