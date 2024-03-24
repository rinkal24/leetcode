class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words_sort = defaultdict()
        
        for ind in range(len(strs)):
            val = ''.join(sorted(strs[ind]))
            if val in words_sort:
                words_sort[val].append(strs[ind])
            else:
                words_sort[val] = [strs[ind]]
                
        res = [x[1] for x in list(words_sort.items())]
        return res