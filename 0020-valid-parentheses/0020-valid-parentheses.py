class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        for i in s:
            if i in ["[", "{","("]:
                stk.append(i)
                
            elif i in ["]", ")", "}"]:
                if len(stk) == 0:
                    return False
                elem = stk.pop()
                if( i == "}" and elem != "{" )or (i == ")" and elem != "(" ) or (i == "]" and elem != "["):
                    return False
                
        if len(stk) > 0:
            return False
        return True