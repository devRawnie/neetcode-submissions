class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = []
        for n in strs:
            l = str(len(n))
            result.append(l + "#" + n)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        i = 0
        tmp = []
        while i < len(s):
            if s[i] != "#":
                tmp.append(s[i])
                i += 1
            else:
                l = int("".join(tmp))
                tmp = []
                result.append(s[i+1:i+l+1])
                i += l+1

        return result

