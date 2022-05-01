class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # two pointer approach by sorting atleast 1 array
#         idx1,idx2=0,0
#         result = set()
#         while idx1<len(nums1) and idx2<len(nums2):
#             if nums1[idx1]==nums2[idx2]:
#                 result.add(nums1[idx1])
#                 idx1+=1
#                 idx2+=1
            
#             elif nums1[idx1]<nums2[idx2]:
#                 idx1+=1
            
#             else:
#                 idx2+=1
        
        
#         return list(result)
                
        result = set()
        seen = set()
        for num in nums1:
            seen.add(num)
        
        for num in nums2:
            if num in seen:
                result.add(num)
        
        return list(result)
            