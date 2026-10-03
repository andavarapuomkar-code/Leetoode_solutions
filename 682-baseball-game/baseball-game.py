class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ops=[]
        for ch in operations:
            if ch == '+':
                ops.append(ops[-1]+ops[-2])
            elif ch == 'D':
                ops.append(2*ops[-1])
            elif ch =='C':
                ops.pop()
            else:
                ops.append(int(ch))
        return sum(ops)
