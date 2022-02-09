class Solution:
    # [题解]1. O(n) t:48ms(76%) O(n) m:14.9M(72%) 哈希
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnts = Counter()
        ans = 0
        for i in nums:
            ans += cnts[i - k] + cnts[i + k]
            cnts[i] += 1
        return ans