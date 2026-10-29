class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        # seen = set([9,1,4,7,3,-1,0,5,8,-1,6])
        # print(seen)
        longestchain = 0
        chain =0

        for num in nums:
            if (num-1) not in seen:
                chain =1
                while num + chain in seen:
                    chain +=1
                longestchain = max(longestchain, chain)
        
        # print(longestchain)
        return longestchain

        