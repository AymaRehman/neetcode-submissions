class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_s = s.strip().lower()
        clean_s = "".join(char for char in clean_s if char.isalnum())

        palindrome = clean_s[::-1]

        if clean_s == palindrome:
            return True

        else:
            return False
