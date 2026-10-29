class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        cleaned = "".join(chars)
        # print(cleaned)
        l =0
        r = len(cleaned)-1
       

        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            l +=1
            r -=1
        # print(cleaned)
        return True
        