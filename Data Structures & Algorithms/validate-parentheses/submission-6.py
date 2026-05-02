class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brack = { "}" : "{", ")" : "(", "]" : "["}
        for char in s:
            if char in brack:
                if stack and stack[-1] == brack[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack