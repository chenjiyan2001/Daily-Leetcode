class Solution:
    # 1. O(n) t:44ms(15%) O(1) m:72%(14.9M) 模拟
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines, cur = 1, 0
        for chr in s:
            new = widths[ord(chr) - ord('a')]
            if 100 - cur < new:
                lines += 1
                cur = new
            else:
                cur += new
        return [lines, cur]