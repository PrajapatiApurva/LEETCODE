class Solution:
    def pivotInteger(self, n: int) -> int:
        temp=math.sqrt(n*(n+1)/2)
        ans=int(temp)
        return ans if temp==ans else -1
        