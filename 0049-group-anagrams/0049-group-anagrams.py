class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words_sort = {}
        
        for ind in range(len(strs)):
            val = ''.join(sorted(strs[ind]))
            if val in words_sort.keys():
                words_sort[val].append(ind)
            else:
                words_sort[val] = [ind]
                
        res = [[] for _ in range(len(words_sort))]
        
        for words in strs:
            val = ''.join(sorted(words))
            ind_val = list(words_sort.keys()).index(val)
            res[ind_val].append(words)
            
        
        return res