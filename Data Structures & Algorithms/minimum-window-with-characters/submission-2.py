#dict_t.items() <= dict_s.items()
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = defaultdict(int)
        for i in t:
            dict_t[i] += 1
        
        left = 0
        result = ""
        dict_s = defaultdict(int)
        for right in range(len(s)):
            dict_s[s[right]] += 1
            curr = ""
            while left <= right and all(key in dict_s and value <= dict_s[key] for key, value in dict_t.items()):
                curr = s[left:right + 1]
                dict_s[s[left]] -= 1
                left += 1

            if len(curr) > 0 and (result == "" or len(curr) < len(result)):
                result = curr

        return result