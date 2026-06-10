class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        maxS = 0
        for lett in s:
            if lett in window:
                index = window.find(lett)
                window = window[index + 1:] 
            window += lett
            maxS = max(maxS, len(window))
        return maxS