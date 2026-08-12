class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {")" : "(",
             "]" : "[",
             "}" : "{"}
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif (not stack) or (stack.pop() != p[s[i]]):
                return False
        if not stack:
            return True
        else:
            return False
    

        
            
        