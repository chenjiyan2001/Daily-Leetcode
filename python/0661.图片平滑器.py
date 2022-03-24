class Solution:
    # 1. O(mnC^2) t:368ms(25%) O(1) m:15.7M(37%) 遍历
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, num = 0, 0
                for x in range(max(i-1, 0), min(i+2, m)):
                    for y in range(max(j-1, 0), min(j+2, n)):
                        tot += img[x][y]
                        num += 1
                ans[i][j] = tot // num
        return ans