class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=dict()
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        s1=set()
        for k,v in freq.items():
            if v in s1:
                return False
            else:
                s1.add(v)
        return True
            


        