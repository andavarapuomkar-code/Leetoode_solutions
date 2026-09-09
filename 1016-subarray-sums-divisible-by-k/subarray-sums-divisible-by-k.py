class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        cnt=0
        mp={0:1}
        for i in nums:
            prefix+=i
            rem=prefix % k
            if rem in mp:
                cnt += mp[rem]
            mp[rem]=mp.get(rem,0)+1
        return cnt