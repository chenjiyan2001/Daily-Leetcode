class Solution:
    # 1. O(n) t:144ms(86%) O(1) m:15.4M(60%) 模拟
    def winnerOfGame(self, colors: str) -> bool:
        d = defaultdict(int)
        cnt = 0
        for c in colors:
            if c == 'A':
                if cnt > 0:
                    cnt += 1
                elif cnt < -2:
                    d['B'] += -cnt - 2
                    cnt = 1
                else:
                    cnt = 1
            else:
                if cnt < 0:
                    cnt -= 1
                elif cnt > 2:
                    d['A'] += cnt - 2
                    cnt = -1
                else:
                    cnt = -1
        if cnt > 2:
            d['A'] += cnt - 2
        elif cnt < -2:
            d['B'] += -cnt - 2
        return d['A'] > d['B']