class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sublist = []
        
        def palindrome(i, j):
            return s[i:j] == s[i:j][::-1]

        def dfs(i, sublist):
            if i == len(s):
                res.append(sublist.copy())
                return
            
            for j in range(i, len(s)):
                if palindrome(i, j + 1):
                    print("here tuye")
                    sublist.append(s[i : j + 1])
                    dfs(j + 1, sublist)
                    sublist.pop()

        dfs(0, sublist)
        return res

        