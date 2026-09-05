import numpy as np
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = np.concatenate((nums1, nums2))
        return np.median(arr)