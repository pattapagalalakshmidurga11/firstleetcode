class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        s=sorted(heights)
        count=0
        for i in range(n):
              if heights[i]!=s[i]:
                count+=1
        return count


        