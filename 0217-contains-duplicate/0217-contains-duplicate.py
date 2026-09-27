class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for x in nums:
            if x not in seen:
                seen.add(x)
            else: return True
        return False