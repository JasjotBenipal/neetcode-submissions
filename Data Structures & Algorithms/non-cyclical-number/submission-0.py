class Solution:
    def isHappy(self, n: int) -> bool:
        sums = set()

        while n not in sums:
            if n == 1:
                return True
            sums.add(n)
            
            store = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                n = n // 10
                store += digit
            
            n = store

        return False    
