class Solution(object):
    def isValid(self, s):
        # method-1:

        # stack = []
        # for ch in s:

        #     if ch in "([{":
        #         stack.append(ch)
            
        #     else:
        #         if not stack:
        #             return False

        #         top = stack.pop()

        #         if ch == ")" and top != "(":
        #             return False

        #         elif ch == "]" and top != "[":
        #             return False

        #         elif ch == "}" and top != "{":
        #             return False

        # return len(stack) == 0

        # Method-2:

        stack = []
        brackets = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in brackets:
                if not stack or stack[-1] != brackets[ch]:
                    return False
                stack.pop()
            else: stack.append(ch)
        return len(stack) == 0