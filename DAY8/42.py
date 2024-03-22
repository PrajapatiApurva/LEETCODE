class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        if n==1 or n==2:
            return 0
        ltor = [0] * n
        rtol = [0] * n
        ltor[0] = height[0]
        for i in range(1, n):
            ltor[i] = max(ltor[i - 1], height[i])

        rtol[n - 1] = height[n - 1]
        for j in range(n - 2, -1, -1):
            rtol[j] = max(rtol[j + 1], height[j])

        for i in range(n):
            water += min(rtol[i], ltor[i]) - height[i]

        return water