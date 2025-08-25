class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        half_len = len(filtered) // 2
        i = 0
        j = len(filtered) - 1

        while i < half_len:
            if filtered[i] != filtered[j]:
                return False
            i += 1
            j -= 1
        return True
