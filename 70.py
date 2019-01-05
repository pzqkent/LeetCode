# 解题思路：

# 爬楼梯问题。经典的动态规划问题。每次上一个台阶或者两个台阶，问一共有多少种方法到楼顶。这个实际上就是斐波那契数列的求解。可以逆向来分析问题，如果有n个台阶，那么走完n个台阶的方式有f(n)种。而走完n个台阶有两种方法，先走完n-2个台阶，然后跨2个台阶；先走完n-1个台阶，然后跨1个台阶。所以f(n) = f(n-1) + f(n-2)。
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        l = [1 for i in range(n+1)]
        for i in range(2,n+1):
            l[i] = l[i-1] + l[i-2]
        return l[n]
