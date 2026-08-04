class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        x, y = a, b
        
        while y != 0:
            x, y = y, x % y

        gcd = x
        lcm = (a * b) // gcd
        
        return [lcm, gcd]