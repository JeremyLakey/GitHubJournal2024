class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 0:
            return "0"

        r = n % (-2)
        if r < 0:
            r = 1 # abs of remainder 
            n = n // (-2) + 1 # round towards zero instead of -inf
        else:
            n = n // (-2)



        return self.baseNeg2(n) + str(r)