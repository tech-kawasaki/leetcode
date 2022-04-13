class Solution:
    def fastPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.fastPow(x, n//2)
        if n%2 == 0:
            return half ** 2
        else:
            return (half ** 2) * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        return self.fastPow(x, n)