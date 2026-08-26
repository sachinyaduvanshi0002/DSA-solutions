class Solution(object):
    def readBinaryWatch(self, turnedOn):
        
        ans = []
        for h in range(12):
            for m in range(60):
                t1 = bin(h).count('1')
                m1 = bin(m).count('1')

                if t1 + m1 == turnedOn:
                    ans.append(str(h) + ":" + str(m).zfill(2))

        return ans