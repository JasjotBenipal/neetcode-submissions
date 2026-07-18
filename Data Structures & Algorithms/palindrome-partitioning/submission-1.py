class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sublist = []
        
        def palindrome(i, j):
            #return s[i:j] == s[i:j][::-1]
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True
            
        def dfs(i, sublist):
            if i == len(s):
                res.append(sublist.copy())
                return
            
            for j in range(i, len(s)):
                #if palindrome(i, j + 1):
                if palindrome(i, j):
                    sublist.append(s[i : j + 1])
                    dfs(j + 1, sublist)
                    sublist.pop()

        dfs(0, sublist)
        return res

        