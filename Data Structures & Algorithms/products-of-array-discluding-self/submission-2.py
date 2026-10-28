class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lf = []
        rg = []
        runningL = 1
        runningR = 1
        ot=[]

        for i in nums:
            lf.append(runningL)
            runningL = runningL * i

        for i in reversed(nums):
            rg.append(runningR)
            runningR = runningR * i
        rg.reverse()
        for k in range(len(nums)):
            ot.append(lf[k] * rg[k])
        return ot
        