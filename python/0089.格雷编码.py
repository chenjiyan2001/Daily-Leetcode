class Solution(object):
    # # 1. O(2^n) t:56ms(36%) m:23.3M(9%) array
    # def grayCode(self, n: int) -> List[int]:
    #     comb = ['0', '1']
    #     for i in range(1, n):
    #         new_comb = ['1' + c.rjust(i, '0') for c in comb[::-1]]
    #         comb.extend(new_comb)
    #     return [int(x, 2) for x in comb]
    
    # 2. O(2^n) t:36ms(95%) m:18.7M(22%) array 首插
    def grayCode(self, n: int) -> List[int]:
        comb = [0, 1]
        num = 1
        for i in range(1, n):
            num *= 2
            new_comb = [num + c for c in comb[::-1]]
            comb.extend(new_comb)
        return comb

    # # 3. O(2^n) t:48ms m:18.4M(27.46) array 尾插
    # def grayCode(self, n: int) -> List[int]:
    #     comb = [0b0]
    #     for i in range(n):
    #         comb = [c << 1 for c in comb]
    #         comb.extend([c + 1 for c in comb[::-1]])
    #     return comb

    # # 4. O(2^n) t:44ms(71%) m:18.4M(28%) 异或
    # def grayCode(self, n: int) -> List[int]:
    #     result = [(i>>1)^i for i in range(2**n)]
    #     return result