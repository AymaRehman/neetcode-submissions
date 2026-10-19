class Solution:
    def isValid(self, s: str) -> bool:

        parentheses_dict = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for p in s:

            if p in parentheses_dict:
                stack.append(p)

            else:
                if not stack:
                    return False

                if parentheses_dict[stack[-1]] != p:
                    return False

                stack.pop()

        return len(stack) == 0
