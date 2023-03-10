from logger import Logger


class Robot:
    def __init__(self, left_motor, right_motor, color_sensor, distance_sensor):
        self.right_m = right_motor
        self.left_m = left_motor
        self.color_sensor = color_sensor
        self.distance_sensor = distance_sensor
        self.logger = Logger("log.txt", self)

    def run(self, speed):
        """
        run the robot at a constant speed
        """
        self.right_m.run(speed)
        self.left_m.run(speed)


    def speed(self):
        return self.right_m.speed() - abs(self.right_m.speed() - self.left_m.speed())

    def color(self):
        return self.color_sensor.color()

    def stop(self):
        self.right_m.hold()
        self.left_m.hold()

    def rotate(self, speed, angle):
        self.left_m.run_angle(speed, -angle * 4, wait=False)
        self.right_m.run_angle(speed, angle * 4)

    def log(self):
        self.logger.log()