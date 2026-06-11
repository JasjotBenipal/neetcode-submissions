class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        for i in s1:
            s1_dict[i] += 1
        
        s2_dict = defaultdict(int)
        s1_len = len(s1)
        left = 0
        for right in range(len(s2)):
            s2_dict[s2[right]] += 1

            while left <= right and (right - left + 1) > s1_len:
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] == 0: del s2_dict[s2[left]]
                left += 1

            if s2_dict == s1_dict:
                return True
        return False