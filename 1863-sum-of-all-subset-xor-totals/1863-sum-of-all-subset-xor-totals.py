class Solution(object):
    def subsetXORSum(self, nums):
        
        def sachin(i, xor):
            if i == len(nums):
                return xor
            
            a = sachin(i+1, xor)

            b = sachin(i+1, xor ^ nums[i])

            return a + b

        return sachin(0, 0)