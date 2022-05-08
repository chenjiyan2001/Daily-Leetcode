class Solution:
    # [题解]1. O(n) t:92ms(67%) O(1) m:21.4M(40%) 原地哈希
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            org = abs(nums[i])
            idx = org - 1
            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                ans.append(org)
        return ans