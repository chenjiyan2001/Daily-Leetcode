class Solution:
    # 1. O(n) t:52ms(78%) O(n) m:15.4M(67%) 哈希
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1, d2 = defaultdict(int), defaultdict(int)
        for idx, i in enumerate(list1):
            d1[i] = idx + 1
        for idx, i in enumerate(list2):
            d2[i] = idx + 1
        minIdx, ans = inf, []
        for k in set(list1) & set(list2):
            idxSum = d1[k] + d2[k] - 2
            if idxSum < minIdx:
                minIdx = idxSum
                ans = [k]
            elif idxSum == minIdx:
                ans.append(k)
        return ans