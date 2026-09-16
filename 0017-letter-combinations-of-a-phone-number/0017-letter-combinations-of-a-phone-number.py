class Solution(object):
    def letterCombinations(self, digits):

        keyboard = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        ans = []
        curr = ""

        def backtrack(idx, curr):
            if idx == len(digits):
                ans.append(curr)
                return
            
            for ch in keyboard[digits[idx]]:
                curr += ch
                backtrack(idx + 1, curr)
                curr = curr[:-1]
            
        backtrack(0, "")
        return ans