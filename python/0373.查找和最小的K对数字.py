from enum import EnumMeta
from turtle import left


class Solution:
    # # 1. O(n^2) 超时
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     res = []
    #     for i in range(len(nums1)):
    #         for j in range(len(nums2)):
    #             res.append([nums1[i], nums2[j]])
    #     return sorted(res, key=sum)[:k]

    # [题解]2. O(n^2) t:1580ms(11%) m:155M(5%)
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     l1, l2 = min(len(nums1), k), min(len(nums2), k)
    #     res = []
    #     for i in nums1[:l1]:
    #         for j in nums2[:l2]:
    #             res.append([i, j])
    #     return sorted(res, key=sum)[:k]

    # [题解]3. O(klogk) t:100ms(34%) m:38.4M(211%) 优先队列/小顶堆
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq, ans = [(num + nums2[0], i, 0) for i, num in enumerate(nums1)], []
        heapq.heapfiy(pq)
        while pq and k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j < len(nums2) - 1:
                heapq.heappush(pq, (nums1[i] + nums2[j+1], i, j+1))
            k -= 1
        return ans

    # [题解]4. O((M+k)logM) M=min(m,n,k) t:64ms(51%) m:26.1M(86%) 多路归并
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        flag, ans = (n := len(nums1)) > (m := len(nums2)), []
        if flag:
            n, m, nums1, nums2 = m, n, nums2, nums1
        pq = []
        for i in range(min(n, k)):
            heapq.heappush(pq, (nums1[i] + nums2[0], i, 0))
        while len(ans) < k and pq:
            _, a, b = heapq.heappop(pq)
            ans.append([nums2[b], nums1[a]] if flag else [nums1[a], nums2[b]])
            if b + 1 < m:
                heapq.heappush(pq, (nums1[a] + nums2[b+1], a, b + 1))
        return ans
    
    # [题解]5. t:488ms m:26.3M(41%) 二分
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        l, r = nums1[0] + nums2[0], nums1[-1] + nums2[-1] + 1
        while l < r:
            mid = (l + r) // 2
            i, j = 0, n-1
            cnt = 0
            while i < m and j >= 0:
                if nums1[i] + nums2[j] > mid:
                    j -= 1
                else:
                    cnt += j + 1
                    i += 1

            if cnt < k:
                l = mid + 1
            else:
                r = mid
        pairSum = l

        ans = []
        # 找数对和小于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] >= pairSum:
                i -= 1
            for j in range(i + 1):
                ans.append([num1, nums2[j]])
                if len(ans) == k:
                    return ans

        # 找数对和等于 pairSum 的数对
        i = n - 1
        for num1 in nums1:
            while i >= 0 and num1 + nums2[i] > pairSum:
                i -= 1
            j = i
            while j >= 0 and num1 + nums2[j] == pairSum:
                ans.append([num1, nums2[j]])
                if len(ans) == k:
                    return ans
                j -= 1
        return ans
