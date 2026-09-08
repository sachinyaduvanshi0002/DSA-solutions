class Solution(object):
    def removeDuplicates(self, s):
        
        ans = []
        for ch in s:
            if ans and ans[-1] == ch:
                ans.pop()
            else:
                ans += ch
        return ''.join(ans)