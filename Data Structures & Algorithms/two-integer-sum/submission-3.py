class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        for i, n in enumerate(nums):
            hMap[n] = i
        i = 0
        while i < len(nums):
            sec = target - nums[i]
            # del hMap[nums[i]]
            if  sec in hMap.keys() and i != hMap[sec]:
                return sorted([i, hMap[sec]])
            else:
                i +=1

        return 0
        

        