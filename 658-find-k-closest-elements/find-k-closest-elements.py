class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans=[]
        for num in arr:
            ans.append(num)
        ans.sort(key=lambda num:abs(num-x))
        ans=ans[:k]
        ans.sort()
        return ans
        