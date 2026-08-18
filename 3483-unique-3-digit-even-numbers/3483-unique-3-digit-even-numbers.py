class Solution(object):
    def totalNumbers(self, digits):
        ans = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and k != i and digits[i] != 0:
                        temp = digits[i] * 100 + digits[j] * 10 + digits[k]

                        if temp % 2 == 0:
                            ans.add(temp)
        
        return len(ans)