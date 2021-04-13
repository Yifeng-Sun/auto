class Mapnode:
    landmark = 0
    x = 0
    y = 0

    def print(self):
        print(str(self.landmark) + " @" + " (" + str(self.x) + ", " + str(self.y) + ")")

    def printlandmark(self):
        print(self.landmark)

    def __init__(self, landmark, x, y):
        self.landmark = landmark
        self.x = x
        self.y = y

