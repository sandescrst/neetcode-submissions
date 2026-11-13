class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hmap1 ={}
        hmap2 = {}

        for i in s1:
            hmap1[i] = hmap1.get(i,0) +1

        for j in range(len(s1)):
            hmap2[s2[j]] = hmap2.get(s2[j], 0) +1

        if hmap1 == hmap2:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            hmap2[s2[left]] -= 1
            if hmap2[s2[left]] ==0:
                del hmap2[s2[left]]

            hmap2[s2[right]] = hmap2.get(s2[right], 0) +1
            left +=1
            
            if hmap1 ==hmap2:
                return True
        return False
        




        print(hmap1, hmap2)

        





  

        