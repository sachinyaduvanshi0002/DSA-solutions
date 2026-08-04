from math import lcm, gcd
class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        return ([lcm(a,b), gcd(a, b)])