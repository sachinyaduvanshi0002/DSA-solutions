class Solution(object):
    def kthCharacter(self, k):
        word = "a"

        while len(word) < k:
            temp = ""

            for ch in word:
                temp += chr(ord(ch) + 1)

            word += temp
        
        return word[k-1]