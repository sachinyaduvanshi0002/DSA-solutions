class Solution(object):
    def calPoints(self, operations):
        
        ans = []
        for i in range(len(operations)):
            if operations[i] == "+":
                a = ans[-1] + ans[-2]
                ans.append(a)
            elif operations[i] == "D":
                b = ans[-1] * 2
                ans.append(b)
            elif operations[i] == "C":
                ans.pop()
            else: ans.append(int(operations[i]))
        
        return sum(ans)