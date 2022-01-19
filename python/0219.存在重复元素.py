class Solution:
    # # 1. O(n) t:88ms O(n) m:24.8M(64%) 滑窗+hash1
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     hash = {}
    #     k += 1
    #     for i in range(min(k, len(nums))):
    #         hash[nums[i]] = hash.get(nums[i], 0) + 1
    #         if hash[nums[i]] == 2: 
    #             return True
    #     for i in range(k, len(nums)):
    #         hash[nums[i-k]] -= 1
    #         hash[nums[i]] = hash.get(nums[i], 0) + 1
    #         if hash[nums[i]] == 2: 
    #             return True
    #     return False

    # [题解]2. O(n) t:84ms O(k) m:22.9M(77%) 滑窗+hash2
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False
