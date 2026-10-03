class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        for ch in s:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        stack1=[]
        for i in t:
            if i=="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        if stack==stack1:
            return True
        else:
            return False