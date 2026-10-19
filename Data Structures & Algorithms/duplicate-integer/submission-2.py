class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        it = 0

        for i in nums:
            if i in hmap:
                return True
            else:
                hmap[i] = it
                it +=1
        return False
