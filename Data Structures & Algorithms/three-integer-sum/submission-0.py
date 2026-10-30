class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        ot = []
        for i in range(len(nums) -2):
            left = i +1
            right = len(nums) -1

            while left < right:
                ts = nums[left] + nums[right]
                if ts > -nums[i]:
                    right -=1
                elif ts < -nums[i]:
                    left +=1
                else:
                    new = [nums[i], nums[left], nums[right]]
                    if new not in ot:
                        ot.append([nums[i], nums[left], nums[right]])
                    left +=1
                    right -=1
                
        return ot

                