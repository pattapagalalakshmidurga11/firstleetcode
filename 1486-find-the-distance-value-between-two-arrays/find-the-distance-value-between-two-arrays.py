class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for x in arr1:
            for y in arr2:
                if abs(x - y) <= d:
                    break
            else:
                count += 1
        return count
        