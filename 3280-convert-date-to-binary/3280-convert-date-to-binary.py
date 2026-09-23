class Solution(object):
    def convertDateToBinary(self, date):
        date = date.split("-")
        y = bin(int(date[0]))[2:]
        m = bin(int(date[1]))[2:]
        d = bin(int(date[2]))[2:]
        return y + "-" + m + "-" + d