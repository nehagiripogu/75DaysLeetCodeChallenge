class Solution(object):
    def reverse(self, x: int) -> int:
        rev = 0
        
        while x != 0:
            # Extract last digit
            digit = x % 10
            
            # Fix Python negative behavior
            if x < 0 and digit > 0:
                digit -= 10
            
            x = (x - digit) // 10
            
            # Overflow check
            if rev > 214748364 or (rev == 214748364 and digit > 7):
                return 0
            if rev < -214748364 or (rev == -214748364 and digit < -8):
                return 0
            
            rev = rev * 10 + digit
        
        return rev