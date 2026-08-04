class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l1=[]
        start=min(nums)
        end=max(nums)
        for i in range(start,end+1):
            if i not in nums:
                l1.append(i)
        return l1
               


        
        