class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        return s

# "5#Hello5#World"
    def decode(self, s: str) -> List[str]:

        li = []
        i = 0
        j =i
        while j <= len(s)-1:
            while s[j] != "#":
                j +=1
            digit = s[i:j]
            length = int(digit)
            start = j+1
            li.append(s[start:start+length])
            i= start+length
            j = i
        return li
