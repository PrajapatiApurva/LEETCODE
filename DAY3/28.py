class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h=len(haystack)
        n=len(needle)
        for i in range(h-n+1):
            temp=haystack[i:i+n]
            if temp==needle:
                return i
        return -1