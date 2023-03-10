from pybricks.pupdevices.Motor



class MyMotor(Motor):
    def forward(self, speed):
        print(self.__dict__)
        pass

    def rotate(self, angle, speed):
        pass

    def stop(self):
        pass