class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq=[0]*101
        maxfreq=0
        for i in nums:
            freq[i]+=1
            maxfreq=max(maxfreq,freq[i])
        ans=0
        for i in freq:
            if i==maxfreq:
                ans+=i
        return ans