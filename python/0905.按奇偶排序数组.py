class Solution:
    # 1. O(nlogn) t:56ms(9%) O(nlogn) m:15.6M(10%) 排序
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:x%2)