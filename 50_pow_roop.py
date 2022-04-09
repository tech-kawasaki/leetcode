class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        current_product = x
        i = n
        while i > 0:
            if (i%2) == 1:
                ans = ans * current_product
            current_product = current_product ** 2
            i //= 2
        return ans