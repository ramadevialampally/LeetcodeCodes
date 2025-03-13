class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
       
        for i in range(len(nums1)):
            flag=True
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    flag=False
                if flag:
                    continue
                else:
                    if nums1[i]<nums2[j]:
                        ans[i]=nums2[j]
                        break
        return ans
                        
        

                
                
        