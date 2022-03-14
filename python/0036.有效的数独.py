class Solution:
    # 1. O(n) t:36ms(96%) O(n) m:15M(57%) 哈希
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d2, d3 = [defaultdict(int) for i in range(9)], [[defaultdict(int) for i in range(3)] for j in range(3)]
        for i in range(9):
            d1 = defaultdict(int)
            for j in range(9):
                num = board[i][j]
                if num == '.': continue
                elif d1[num] > 0: return False
                elif d2[j][num] > 0: return False
                elif d3[i // 3][j // 3][num] > 0: return False
                d1[num] = 1
                d2[j][num] = 1
                d3[i // 3][j // 3][num] = 1
        return True