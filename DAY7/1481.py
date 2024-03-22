class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        print(c)
        print((sorted(c.values())))
        for i,v in enumerate(sorted(c.values())):
            k-=v
            if k<0:
                return len(c) -i
        return 0