def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    return 0
    
    
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
for i in range(n):
    nums1[m+i] = nums2[i]
nums1.sort()

    
    
print(nums1)
#merge(nums1, m, nums2, n)