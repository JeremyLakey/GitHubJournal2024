
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        answers = []

        for r in range(rows):
            for c in range(cols):
                answers.append((r, c))
        return sorted(answers, key=lambda x: (abs(rCenter - x[0]) + abs(cCenter - x[1])))
        