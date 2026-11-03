class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hmap = {}
        longest = 1

        for right in range(len(s)):
            hmap[s[right]] = hmap.get(s[right],0) +1

            while ((right -left +1) - max(hmap.values())) >k:
                hmap[s[left]] -=1
                left +=1
            
            longest = max(longest, (right - left) +1)

        return longest