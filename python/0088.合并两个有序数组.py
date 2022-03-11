class Solution:
    # 1. O(m+n) t:36ms(57%) O(1) m:14.9M(63%) 双指针
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        i = len(nums1) - 1
        while m >= 0 or n >= 0:
            if m < 0: 
                nums1[i] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[i] = nums1[m]
                m -= 1
            elif nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1