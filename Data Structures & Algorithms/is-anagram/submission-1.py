class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        y =sorted(s)
        z =sorted(t)
        if y == z:
            return True
        return False
        