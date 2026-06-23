class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = str(len(strs)) + "~@~"+ "~0~".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split("~@~")
        l = int(decoded[0])
        if l == 0:
            return []
        data = decoded[1]
        res = data.split("~0~")
        return res
