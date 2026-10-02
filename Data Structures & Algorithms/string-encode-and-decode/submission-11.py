class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        
        for word in strs:
            res += str(len(word))
            res += "#" + word
        return res
    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            j = ""
            size = 0
            while s[l] != "#":
                j += s[l]
                l+=1
            l += 1
            size = int(j)
            res.append(s[l: l + size])
            l += size
        return res
