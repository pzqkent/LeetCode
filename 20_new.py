class Solution(object):
    def isValid(self, s):
        if s == []:
            return False
        elif len(s) % 2 == 1:
            return False
        stack = []
        a = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in a.values():
                stack.append(i)
            else:
                if a[i] in stack:
                    stack.pop(-1)
                else:
                    return False
        if stack == []:
            return True
        else:
            return False

思路：
生成一个stack。
遍历字符串中的每一个符号，如果该符号在['(','[','{']中，则将该字符串加入stack。
    否则，如果该符号所对应的另一半在stack中，则pop该stack中最后一个进入的元素
        否则，返回false
当遍历完字符串中的所有符号后，如果stack为空，则返回true，否则返回false

