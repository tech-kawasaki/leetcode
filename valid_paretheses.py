class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["{", "(", "["]:
                stack.append(i)
            elif i in ["}", ")", "]"] and len(stack) > 0:
                p = stack.pop()
                if not((i == "}" and p == "{") or (i == ")" and p == "(") or (i == "]" and p == "[")):
                    return False
            else:
                return False
        return len(stack) == 0