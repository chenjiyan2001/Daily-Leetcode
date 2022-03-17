class Solution:
    # [题解]1. O(llogn) t:44ms(83%) O(l) m:15.4M(61%) 模拟
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x:(-len(x), x), reverse=True)
        longest = ""
        candidates = {""}
        for w in words:
            if w[:-1] in candidates:
                longest = w
                candidates.add(w)
        return longest