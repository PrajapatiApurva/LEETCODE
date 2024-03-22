class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp=list(s.strip().split())
        return len(temp[-1])