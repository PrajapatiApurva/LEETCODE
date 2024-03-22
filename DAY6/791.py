class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ch_freq = {ch: 0 for ch in order}

        for ch in s:
            if ch in ch_freq:
                ch_freq[ch] += 1
    
        ans = ''
        for ch in order:
            ans += ch * ch_freq[ch]
    
        for ch in s:
            if ch not in order:
                ans += ch

        return ans