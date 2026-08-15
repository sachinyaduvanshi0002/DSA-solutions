class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        pf = strs[0]

        for s in strs[1:]:
            while not s.startswith(pf):
                pf = pf[:-1]
        
        return pf