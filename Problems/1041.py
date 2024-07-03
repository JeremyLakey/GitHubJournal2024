class Solution(object):

    # 0 is north
    # 1 is east
    # 2 is south
    # 3 is west
    def turnRight(self, d):
        if d < 3:
            return d + 1
        else:
            return 0

    def turnLeft (self, d):
        if d > 0:
            return d - 1
        else:
            return 3

    def go(self, x, y, d):
        if d == 0:
            return x, y + 1
        elif d == 1:
            return x + 1, y
        elif d == 2:
            return x, y - 1
        else:
            return x - 1, y

    def running(self, x, y, d, i, instructions):
        if i < len(instructions):
            iy = instructions[i]
            if iy == "G":
                x2, y2 = self.go(x, y, d)
                return self.running(x2, y2, d, i + 1, instructions)
            if iy == "L":
                d2 = self.turnLeft(d)
                return self.running(x, y, d2, i + 1, instructions)
            if iy == "R":
                d2 = self.turnRight(d)
                return self.running(x, y, d2, i + 1, instructions)
        else:
            return (x, y, d) 

    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """

        x, y, d = self.running(0, 0, 0, 0, instructions)

        return (x == 0 and y == 0) or d != 0


        