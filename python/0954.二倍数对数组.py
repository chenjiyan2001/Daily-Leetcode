class Solution:
    # [题解]1. O(nlogn) t:108ms(78%) O(n) m:16.9M(66%) 排序+哈希表计数
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        cnts = Counter(arr)
        for num in list(cnts.keys()):
            if num > 0 and cnts[num * 2] < cnts[num]:
                return False
            elif num > 0:
                cnts[num * 2] -= cnts[num]
            elif num < 0 and cnts[num / 2] < cnts[num]:
                return False
            elif num < 0:
                cnts[num / 2] -= cnts[num]
            elif num == 0 and cnts[num] % 2:
                return False
        return True