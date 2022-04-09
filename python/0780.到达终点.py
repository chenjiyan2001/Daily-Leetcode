class Solution:
    # [题解]1. O(log max(tx, ty)) t:36ms(44%) O(1) m:14.9M(64%) 反向计算
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            tx, ty = (tx % ty, ty) if tx > ty else (tx, ty % tx)
        if tx == sx and ty == sy:
            return True
        elif tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        elif ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        else:
            return False