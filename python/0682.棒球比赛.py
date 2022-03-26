class Solution:
    # [题解]1. O(n) t:32ms(92%) O(n) m:15.1M(90%) 模拟
    def calPoints(self, ops: List[str]) -> int:
        records = []
        for op in ops:
            match op:
                case "D":
                    records.append(records[-1] * 2)
                case "C":
                    records.pop()
                case "+":
                    records.append(records[-1] + records[-2])
                case _:
                    records.append(int(op))
        return sum(records)