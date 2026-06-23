class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "<>"

        result = []
        for s in strs:
            s_int = [str(ord(c)) for c in s]
            result.append(",".join(s_int))

        return "#".join(result)

    def decode(self, s: str) -> List[str]:
        if s == "<>":
            return []
        words = s.split("#")
        result = []
        for w in words:
            s_chr = [chr(int(c)) for c in w.split(",") if c]
            result.append("".join(s_chr))

        return result
