import time


class Logger:
    def __init__(self, filename, robot):
        self.robot = robot
        self.file = open(filename, "w")
        self.file.write(",".join(["time", "speed", "color"]))


    def log(self):
        self.file.write(",".join([str(time.time()), str(self.robot.speed()), str(self.robot.color())]))

    def close(self):
        self.file.close()
