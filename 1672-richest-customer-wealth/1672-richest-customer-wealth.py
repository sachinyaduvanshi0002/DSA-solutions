class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth=0
        for customers in accounts:
            wealth=sum(customers)
            max_wealth=max(max_wealth, wealth)
        return max_wealth