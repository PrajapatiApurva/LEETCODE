class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1=sorted(s)
        n2=sorted(t)
        return n1 == n2

        