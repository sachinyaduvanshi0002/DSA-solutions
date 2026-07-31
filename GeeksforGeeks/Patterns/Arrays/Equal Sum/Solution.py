class Solution:
	def equilibrium(self,arr): 
    	# code here
    	total = sum(arr)
    	leftsum = 0
    	for i in range(len(arr)):
    	    total -= arr[i]
    	    
    	    if leftsum == total:
    	        return "true"
    	        
    	    leftsum += arr[i]
        return "false"