# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        # 纯数字
        if s[0] != '[':
            return NestedInteger(int(s))
        stack, curVal, sign = [], 0, False
        for i, c in enumerate(s):
            match c:
                case '[':
                    # 递归嵌套
                    stack.append(NestedInteger())
                case '-':
                    # 数字符号
                    sign = True
                case ',':
                    # 只有上一个字符是数字才加入了新的数字，否则可能是 "],"
                    if s[i - 1].isdigit():
                        stack[-1].add(NestedInteger(-curVal if sign else curVal))
                    curVal, sign = 0, False
                case ']':
                    # 只有上一个字符是数字才加入了新的数字，否则可能是 "[]"
                    if s[i - 1].isdigit():
                        stack[-1].add(NestedInteger(-curVal if sign else curVal))
                    # 弹出栈，并将当前的对象加入嵌套的列表中
                    if len(stack) > 1:
                        cur = stack.pop()
                        stack[-1].add(cur)
                    curVal, sign = 0, False
                case _:
                    # 数字计算
                    curVal = curVal * 10 + int(c)
        return stack.pop()
