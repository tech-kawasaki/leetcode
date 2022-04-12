class Solution:
    def myPow(self, x, n):
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        ans = 1
        for _ in range(N):
            ans = ans * x
        return ans