class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_window = defaultdict(int)

        result = 0
        left = 0

        for right in range(len(s)):
            count_window[s[right]] += 1
            print(f"count for: {s[right]} is: {count_window[s[right]]}")
            
            while left <= right and ((right - left + 1) - max(count_window.values())) >k:
                count_window[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        return result

