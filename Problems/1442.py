class Solution(object):
    def xorRange(self, a, b, precal):
        if a == 0:
            return precal[b]
        else:
            return precal[a - 1] ^ precal[b]

    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        precal = [0 for _ in range(len(arr))]
        precal[0] = arr[0]
        for x in range(1, len(arr)):
            precal[x] = precal[x - 1] ^ arr[x]

        count = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if self.xorRange(i, j-1, precal) == self.xorRange(j, k, precal):
                        count+=1
        return count

class Solution2(object):
    def xorRange(self, a, b, precal):
        if a == 0:
            return precal[b]
        else:
            return precal[a - 1] ^ precal[b]

    def addToMappy(self, a, b, precal, mappy):
        if a == 0:
            v = precal[b]
            if v in mappy[a]:
                mappy[a][v] += 1
            else:
                mappy[a][v] = 1
        else:
            v = precal[a - 1] ^ precal[b]
            if v in mappy[a]:
                mappy[a][v] += 1
            else:
                mappy[a][v] = 1


    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        precal = [0 for _ in range(len(arr))]
        precal[0] = arr[0]
        for x in range(1, len(arr)):
            precal[x] = precal[x - 1] ^ arr[x]
        mappy = [{} for _ in range(len(arr))]

        for i in range(1, len(arr)):
            for j in range(i, len(arr)):
                self.addToMappy(i, j, precal, mappy)

        count = 0

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                v = self.xorRange(i, j - 1, precal)
                if v in mappy[j]:
                    count += mappy[j][v]
        return count
