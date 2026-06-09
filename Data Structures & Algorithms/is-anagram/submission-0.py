class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            storeS = {}
            storeT = {}

            for index in range(len(s)):
                storeS[s[index]] = storeS.get(s[index], 0) + 1
                storeT[t[index]] = storeT.get(t[index], 0) + 1
            return storeS == storeT
