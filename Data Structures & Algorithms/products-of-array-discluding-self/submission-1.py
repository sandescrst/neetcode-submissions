class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prdLeft = []
        prdRight = []
        runningPrdL = 1
        runningPrdR=1
        ot = []

        for i in nums:
            prdLeft.append(runningPrdL)
            runningPrdL= runningPrdL * i
        # print(prdLeft)
        for j in reversed(nums):
            prdRight.append(runningPrdR)
            runningPrdR = runningPrdR *j
        prdRight.reverse()
        # print(prdRight)
        for k in range(len(nums)):
            ot.append(prdLeft[k] * prdRight[k])
        
        return ot
