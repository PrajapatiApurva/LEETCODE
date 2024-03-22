class Solution:
    def reverse(self, x: int) -> int:   
        flag=1
        if x<0:
            flag=0
            x=-x
        temp=x
        count=0
        while(temp):
            count+=1
            temp//=10
        temp=x
        ans=0
        while(temp):
            rem=temp%10
            ans=(ans*10)+rem
            temp//=10
        if -2**31>=ans or ans>=(2**31)-1:
            return 0
        return ans if flag else -ans
