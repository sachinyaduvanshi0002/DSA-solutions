# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):

        def bt(root):
            if not root: return None
            mid = len(root)//2

            tree = TreeNode(root[mid])

            tree.left = bt(root[:mid])
            tree.right = bt(root[mid+1:])

            return tree
            
        return bt(nums)