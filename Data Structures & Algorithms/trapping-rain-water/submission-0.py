class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max =[]
        tallest = 0
        tallest_r=0
        total = 0
        # amt = abs(l-r)
        
        for h in height:
            left_max.append(tallest)
            tallest = max(tallest,h)
        
        for h in reversed(height):
            right_max.append(tallest_r)
            tallest_r = max(tallest_r,h)
        right_max.reverse()
        for i in range(len(height)):
            total += max(0, min(left_max[i],right_max[i])- height[i])
        
        return total




        