class Solution(object):
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def backtrack(start, target):
            
            if target == 0:
                ans.append(temp[:])
                return
            
            if target < 0: return

            for i in range(start, len(candidates)):
                temp.append(candidates[i])
                
                backtrack(i, target - candidates[i])

                temp.pop()

        backtrack(0, target)   
        return ans