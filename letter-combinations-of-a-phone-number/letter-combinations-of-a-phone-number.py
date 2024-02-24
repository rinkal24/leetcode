class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        phone_dict = {"2":["a", "b", "c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        
        def backtrack(index, path):
            if len(digits) == len(path):
                res.append("".join(path))
                return
            
            letters = phone_dict[digits[index]]
            
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
                
            
        res = []
        backtrack(0,[])
        return res
        