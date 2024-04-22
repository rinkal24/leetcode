import random
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        
        last_ele, ind = self.l[-1], self.d[val]
        self.l[ind], self.d[last_ele] = last_ele, ind
        
        self.l.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()