class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit=0
        minimum=prices[0]+fee
        for i in prices:
            if minimum<i:
                profit+=i-minimum
                minimum=i
            elif i+fee<minimum:
                minimum=i+fee
        return profit