class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)

        while i < n-1:
            if bits[i] == 0:
                i += 1
            else: i += 2
        
        return i == n-1