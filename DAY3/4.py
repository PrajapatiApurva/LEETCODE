class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        f=len(nums1)
        s=len(nums2)
        i=0
        j=0
        m1=0
        m2=0

        for num in range((s+f)//2+1):
            m2=m1
            if i<f and j<s:
                if nums1[i]>nums2[j]:
                    m1=nums2[j]
                    j+=1
                else:
                    m1=nums1[i]
                    i+=1
            elif i<f:
                m1=nums1[i]
                i+=1
            else:
                m1=nums2[j]
                j+=1
        if (f+s)%2==1:
            return float(m1)
        return float(m1+m2)/2.0