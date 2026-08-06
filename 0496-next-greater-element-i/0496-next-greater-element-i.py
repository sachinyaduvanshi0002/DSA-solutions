class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j + 1
                    while k < len(nums2):
                        if nums2[k] > nums2[j]:
                            ans.append(nums2[k])
                            break
                        k += 1
                    else: ans.append(-1)
        return ans