class Solution(object):
    def toHex(self, num):
        freq = {
            10 : "a",
            11 : "b",
            12 : "c",
            13 : "d",
            14 : "e",
            15 : "f"
        }
        ans = ""

        if num == 0: return "0"

        if num < 0:
            num += 2**32
            
        while num > 0:
            digit = num % 16
            if digit in freq:
                ans += freq[digit]
            else: ans += str(digit)

            num //= 16
        return ans[::-1]