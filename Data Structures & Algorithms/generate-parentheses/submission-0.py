class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, close, substr):
            if open == n and close == n:
                res.append(substr)
                print("res")
                return
            
            # Case1 : include (
            if open < n:
                substr += "("
                print("open")
                backtrack(open + 1, close, substr)
                substr = substr[:-1]

            # Case 2: include )
            #substr = substr[:-1]
            if close < open:
                substr += ")"
                print("close")
                backtrack(open, close + 1, substr)
                substr = substr[:-1]

        backtrack(0, 0, "")
        return res