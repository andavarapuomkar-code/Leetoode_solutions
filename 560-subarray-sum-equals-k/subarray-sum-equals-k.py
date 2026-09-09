class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        cnt=0
        mp={0:1}
        for i in nums:
            prefix +=i
            if prefix - k in mp:
                cnt += mp[prefix-k]
            mp[prefix]=mp.get(prefix,0)+1
        return cnt
    