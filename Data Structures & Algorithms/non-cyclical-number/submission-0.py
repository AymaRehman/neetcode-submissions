class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            sq = 0

            for digit in str(n):
                sq += int(digit) ** 2

            n = sq

        return True
