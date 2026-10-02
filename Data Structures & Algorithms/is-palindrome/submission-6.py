class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = re.sub(r"[^a-zA-z0-9]", "", s)
        l,r = 0, len(cleaned) - 1
        while l <= r:
            if cleaned[l].upper() != cleaned[r].upper():
                return False
            else:
                l += 1
                r -= 1
        return True