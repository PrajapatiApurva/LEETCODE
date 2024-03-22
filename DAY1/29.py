class Solution:
    def divide(self, d: int, di: int) -> int:
        if d==-2147483648 and di==-1:
            return -d-1

        return math.floor(d/di) if (di>0 and d>0)or(d<=0 and di<0) else math.ceil(d/di)
        