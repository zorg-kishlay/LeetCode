class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        end1=len(nums1)-1 # end of first list
        end2= len(nums2)-1 # end of 2nd list
        
        end0= len(nums1)-len(nums2)-1 # index of last non zero element in nums1
        
        while end0>=0 and end2>=0:
            if nums1[end0]>nums2[end2]:
                nums1[end1]=nums1[end0]
               
                end0-=1
            
            elif nums1[end0]<=nums2[end2]:
                nums1[end1]=nums2[end2]
                end2-=1
            end1-=1
        
        
        # if nums1 exhausts before nums2  nums1=[7 8 9 0 0 0] and nums2=[1 2 3]
        # then after the above step it should be nums1=[7 8 9 7 8 9]
        while end2>=0 and end1>=0:
            nums1[end1]=nums2[end2]
            end2-=1
            end1-=1
        