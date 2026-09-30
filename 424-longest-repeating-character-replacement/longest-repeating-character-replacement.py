from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        l = 0
        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(freqs.values())
            curLen = j - l + 1
            if curLen - maxFreq > k:
                freqs[s[l]] -= 1
                l += 1
            res = max(res, j - l + 1)
        return res