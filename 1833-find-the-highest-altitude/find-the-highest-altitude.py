class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt=0
        high=0
        for x in gain:
            alt+=x
            high=max(high,alt)
        return high