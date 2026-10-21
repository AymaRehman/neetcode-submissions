class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        length = len(digits) - 1
        last_digit = digits[length]

        if last_digit < 9:
            digits[length] += 1
        else:
            i = length

            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1

            if i >= 0:
                digits[i] += 1
            else:
                digits.insert(0, 1)

        return digits
