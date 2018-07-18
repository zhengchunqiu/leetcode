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
    
    
    #3.二分查找一个i满足:<1>.A[i-1]<B[j],B[j-1]<A[i];<2>.j=(m+n+1)/2-i
    
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m
        if n==0:
            return ValueError
        
        imin,imax=0,m
        half_len=(m+n+1)//2
        while imin<imax:
            i=(imin+imax)//2
            j=half_len-i
            if i<m and nums1[i]<nums2[j-1]:
                imin=i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if i==0:
                    max_of_left=nums2[j-1]
                elif j==0:
                    max_of_left=nums1[i-1]
                else:
                    max_of_left=max(nums1[i-1],nums[j-1])
                if (m+n)%2==1:
                    return max_of_left
                
                if i==m:
                    min_of_right=nums2[j]
                elif j==0:
                    min_of_right=nums1[i]
                else:
                    min_of_right=min(nums1[i],nums2[j])
                  
                return (max_of_right+min_of_right)/2.0    
