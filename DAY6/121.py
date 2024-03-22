class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=float('inf')
        ma=0
        for p in prices:
            if p<m:
                m=p
            elif p-m>ma:
                ma=p-m
        return ma


        # n=len(prices)
        # if n==1:
        #     return 0
        # l=0
        # r=1
        # ans=0
        # while r<n:
        #     temp=prices[r]-prices[l]
        #     if prices[l]<prices[r]:
        #         ans=temp if temp>ans else ans
        #     else:
        #         l=r
        #     r+=1
        # return ans 