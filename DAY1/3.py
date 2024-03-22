# Easy
# 3. Longest Substring Without Repeating Characters
# Time-complexity:O(n)
# Space-complexity:O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        ans = ""
        start,end = 0,0
        ci = {}

        while end < len(s):
            c = s[end]
            if c not in ci:
                ci[c] = end  
            else:
                if ci[c]+ 1 > start:
                    start = ci[c]+1
                ci[c] = end
            
            if len(ans) < end-start+1:
                ans = s[start:end+1]

            end += 1
        
        if len(ans) < end-start:
            ans = s[start:end]  

        return len(ans)


