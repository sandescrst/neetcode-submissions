class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hSet = set()

         for i in nums:
            if i in hSet:
                return True
            else:
                hSet.add(i)

         return False