class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s = s+ str((len(word)) )+ "#" + word
        # print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        j =i
        while j<= len(s)-1:
            while s[j] != "#":
                j +=1
            digits = s[i:j]
            length = int(digits)
            start = j+1
            strs.append(s[start:start+length])
            i = start + length
            j = i
        return strs
