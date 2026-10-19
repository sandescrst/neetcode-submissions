class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmaps={}
        hmapt={}

        for i in s:
            hmaps[i] =  hmaps.get(i, 0) +1

        for j in t:
            hmapt[j] = hmapt.get(j,0)+1

        return hmaps == hmapt


        