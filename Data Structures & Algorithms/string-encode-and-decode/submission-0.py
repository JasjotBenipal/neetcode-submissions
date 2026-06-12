class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for one_string in strs:
            result += str(len(one_string)) + "#" + one_string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        if s == "":
            return list(s)
        
        index = 0
        while index < len(s):
            jedex = index

            while s[jedex] != "#":
                jedex += 1

            length = int(s[index:jedex])
            
            result.append(s[jedex + 1 : jedex + 1 + length])
            index = jedex + 1 + length
        
        return result
