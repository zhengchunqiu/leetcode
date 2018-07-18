#1.合并两个已排序数组    104ms,81.62%
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        result+=nums1[i:]
        result+=nums2[j:]
        index=len(result)
        if index%2==1:
            ans=result[index//2]
        else:
            ans=(result[index//2-1]+result[index//2])/2
        return ans
        
 #2.nums=sorted(nums1+nums2)排序      92ms,99.94%
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result=sorted(nums1+nums2)
        index=len(result)
        if index%2==1:
            ans=result[index//2]
        else:
            ans=(result[index//2-1]+result[index//2])/2
        return ans        
        
