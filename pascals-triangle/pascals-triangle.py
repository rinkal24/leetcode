class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numExtra = 0
        res = [[1]]
        for i in range(1, numRows):
            temp_res = []
            temp_res.append(1)
            tempExtra = numExtra
            ptr1 = 0
            
            while(tempExtra > 0):
                temp_res.append(res[i - 1][ptr1] + res[i - 1][ptr1 + 1])
                ptr1 += 1
                tempExtra -= 1
                
            temp_res.append(1)
            res.append(temp_res)
            numExtra += 1
        
        return res
            