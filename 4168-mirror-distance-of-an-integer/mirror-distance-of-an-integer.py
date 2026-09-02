class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp=n
        revnum=0
        while n>0:
            d=n%10
            revnum=revnum*10+d
            n//=10
        return abs(temp-revnum)

        