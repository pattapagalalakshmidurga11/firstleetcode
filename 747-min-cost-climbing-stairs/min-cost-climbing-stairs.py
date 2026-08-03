class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        a=0
        b=0
        for i in range(2,n+1):
            a,b=b,min(cost[i-2]+a,cost[i-1]+b)
        return b

        