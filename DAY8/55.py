class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        main=n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=main:
                main=i
        return True if main==0 else False