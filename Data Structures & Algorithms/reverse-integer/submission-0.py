class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * sign
        while x:
            res = res * 10 + (x % 10)
            x = x // 10
        
        if -2147483648 > res or res > 2147483647:
            return 0
        return sign * res