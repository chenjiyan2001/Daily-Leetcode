class Solution:
    # 1. O(n) t:92ms(17%) O(n) m:25.4M(29%) 哈希表
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if Counter(nums).most_common(1)[0][1] > 1 else False
    
    # ...