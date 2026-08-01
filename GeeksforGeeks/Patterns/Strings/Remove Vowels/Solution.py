class Solution:
	def removeVowels(self, s):
		# code here
		vowels = "aeiou"
		res = ""
		for ch in s:
		    if ch in vowels: continue
		    else: res += ch
	    return res