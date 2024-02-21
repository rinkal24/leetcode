class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        charStack = []
        charStackFlag = False
        countStackFlag = True
        countVal = ''
        curr_Str = ''
        
        for i in range(len(s)):
            if s[i].isnumeric():
                countVal += s[i]
            elif s[i].isalpha():
                curr_Str += s[i]
            elif s[i] == "[":
                charStack.append(curr_Str)
                countStack.append(int(countVal))
                curr_Str = ''
                countVal = ''
            elif s[i] == "]":
                curr_count = countStack.pop()
                decoded_str = charStack.pop()
                decoded_str += curr_Str * curr_count
                curr_Str = decoded_str
            else:
                curr_Str += s[i]
               
        return curr_Str
                