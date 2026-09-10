class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move left until it points to a letter
            if not s[left].isalpha():
                left += 1
            
            # Move right until it points to a letter
            elif not s[right].isalpha():
                right -= 1
            
            # Both are letters → swap
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)