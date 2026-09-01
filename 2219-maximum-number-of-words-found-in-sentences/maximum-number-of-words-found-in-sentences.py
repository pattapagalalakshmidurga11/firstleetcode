class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxcount=0
        for sentence in sentences:
            if len(sentence.split())>maxcount:
                maxcount=len(sentence.split())
        return maxcount