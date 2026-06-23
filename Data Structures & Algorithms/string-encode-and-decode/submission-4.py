class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        return ";".join(list(map(lambda x: "*" if x == "" else ",".join([str(ord(i)) for i in x]), strs)))

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        return list(map(lambda x: "" if x == "*" else "".join([chr(int(i)) for i in x.split(",")]), s.split(";")))
