
class Solution:

    def helper(self, n: int) -> str:
        if n == 3:
            return "11"
        if n == 2:
            return "10"
        if n == 1:
            return "01"
        if n == 0:
            return "1"


    def baseNeg2(self, n: int) -> str:
        # Base 4
        # 0 === 100 = 4
        # 3 === 111 = 3
        # 2 === 110 = 2
        # 1 === 001 = 1
        # 0 === 000 = 0

        if n == 4:
            return "100"
        if n == 3:
            return "111"
        if n == 2:
            return "110"
        if n == 1:
            return "1"
        if n == 0:
            return "0"

        t = ""
        while n > 0:
            m = n % 4
            t = self.helper(n % 4) + t
            n /= 4

