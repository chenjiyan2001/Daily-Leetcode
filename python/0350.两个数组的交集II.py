class Solution:
    # 1. O(n) t:32ms(90%) O(n) m:15M(78%) 哈希
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = Counter(nums1), Counter(nums2)
        ans = []
        for k in set(nums1.keys()) & set(nums2.keys()):
            ans.extend([k] * min(nums1[k], nums2[k]))
        return ans

    # 2. O(n) t:40ms(53%) O(1) 双指针
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        m, n = len(nums1), len(nums2)
        i, j = 0, 0 
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans