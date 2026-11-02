class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        # mh = 1
        num = min(heights[l], heights[r])
        mh = num * (r-l)

        while l<r:
            
            # print([num, mh])

            if heights[l] < heights[r]:
                l +=1
                num = min(heights[l], heights[r])
                temp = num * (r-l)
                mh = max(mh, temp)
                print(mh)

            else: 
                r -=1
                num = min(heights[l], heights[r])
                temp = num * (r-l)
                mh = max(mh, temp)

        return mh  

            
            
        