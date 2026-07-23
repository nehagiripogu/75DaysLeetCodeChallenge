class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fib(n):
            if n==1 or n==0:
                return n
            return fib(n-1)+fib(n-2)
        res=fib(n)
        return res