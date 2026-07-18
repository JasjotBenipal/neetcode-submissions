class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: return res

        digitToChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, substr):
            if i == len(digits):
                res.append(substr)
                return
            
            for j in digitToChar[digits[i]]:
                substr += j
                dfs(i + 1, substr)
                substr = substr[:-1]

        dfs(0, "")
        return res