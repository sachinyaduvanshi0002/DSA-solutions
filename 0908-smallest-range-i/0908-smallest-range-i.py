class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = max(nums)
        s = min(nums)
        newl = l-k
        news = s+k
        return max(0, newl - news)