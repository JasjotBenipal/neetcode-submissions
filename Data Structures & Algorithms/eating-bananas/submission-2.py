class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        num = 0
        maxi = 0
        for i in piles:
            num += i
            maxi = max(maxi, i)
        num = math.ceil(num / h)

        left, right = num, maxi
        result = maxi
        while left <= right:
            mid = (left + right) // 2
            total = 0
            for i in piles:
                total += math.ceil(i / mid)
            
            if total <= h:
                right = mid - 1
                result = min(result, mid)
            elif total > h:
                left = mid + 1
        return result
        