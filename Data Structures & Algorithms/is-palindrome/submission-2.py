class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(char for char in s if char.isalnum())
        ss = ss.lower()

        return ss == ss[::-1]
