class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        while l<h:
            mid=(l+h)//2
            def canfish(weights,days,mid):
                reqdays=1
                load=0
                for wt in weights:
                    if load+wt<=mid:
                        load+=wt
                    else:
                        reqdays+=1
                        load=wt
                return reqdays <= days
            noofdays=canfish(weights,days,mid)
            if noofdays:
                h=mid
            else:
                l=mid+1
        return l