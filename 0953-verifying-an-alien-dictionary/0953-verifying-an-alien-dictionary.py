class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        for i in range(len(words) - 1):
            ind = 0
            l1 = words[i][ind]
            l2 = words[i + 1][ind]
            if l1 == l2:
                while ind < len(words[i]) and ind < len(words[i + 1]):
                    l1 = words[i][ind] 
                    l2 = words[i + 1][ind] 
                    #print(l1, l2)
                    if (l1 and l2 not in order) or (order.index(l1) > order.index(l2)):
                        #print('here', l1, l2)
                        return False
                    ind += 1
                if len(words[i]) > len(words[i + 1]) and l1 == l2:
                    return False
            elif order.index(l1) > order.index(l2):
                return False
        return True