class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        a=sum(aliceSizes)
        b=sum(bobSizes)
        diff=(b-a)//2
        bob=set(bobSizes)
        for a in aliceSizes:
            b=a+diff
            if b in bob:
                return [a,b]