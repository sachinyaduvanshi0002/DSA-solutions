class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)

        if n % 2 != 0:
            ans = nums1[n // 2]
        else: ans = (nums1[n//2 - 1] + nums1[n//2]) / float(2)

        return ans