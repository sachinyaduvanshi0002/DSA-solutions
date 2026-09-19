class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()

        ans = []
        temp = []

        def backtrack(start, target):
            if target == 0:
                ans.append(temp[:])
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > target:
                    break

                temp.append(candidates[i])

                backtrack(i+1, target - candidates[i])

                temp.pop()
            
        backtrack(0, target)
        return ans