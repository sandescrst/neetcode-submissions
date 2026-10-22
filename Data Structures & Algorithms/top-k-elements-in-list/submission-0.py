class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stor= {}
        bucket=[[] for _ in range(len(nums) +1)]
        otpt= []
        for i in nums:
            if i not in stor:
                stor[i] = 0
            stor[i] +=1
        # print(stor)
        for keys, val in stor.items():
            bucket[val].append(keys)
        for itm in range(len(bucket)-1,0,-1):
            for el in bucket[itm]:
                if k>0:
                    otpt.append(el)
                    k -=1
                
        return otpt
        


        
        # print(bucket)   
                

            
            

        