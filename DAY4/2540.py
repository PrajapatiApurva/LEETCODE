class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        n1=len(nums1)
        n2=len(nums2)
        while i<n1 and j<n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums2[j]<nums1[i]:
                j+=1
            else:
                i+=1
        return -1