class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        mh = 0
        

        while l<r:
            temp = min(heights[l], heights[r]) * (r-l)
            mh = max(mh, temp)
            
            # print([num, mh])

            if heights[l] < heights[r]:
                l +=1
                # num = min(heights[l], heights[r])
                # temp = num * (r-l)
                # mh = max(mh, temp)
                # # print(mh)

            else: 
                r -=1
                # num = min(heights[l], heights[r])
                # temp = num * (r-l)
                # mh = max(mh, temp)

        return mh  

            
            
        