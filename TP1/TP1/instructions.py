import time


class InstructionSet:
    def __init__(self, instructions):
        self.instructions = instructions
        self.current = self.instructions[0]
        self.current.started_at = time.time()

    def prepend():
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.current.is_ended():
            del self.instructions[0]
            self.current = self.instructions[0]
            self.current.started_at = time.time()
        return self.current
            
        
class Instruction:
    def __init__(self, robot, duration):
        self.robot = robot
        self.started_at = None
        self.duration = duration

    def is_ended(self):
        return time.time() - self.started_at >= self.duration


class Forward(Instruction):
    def __init__(self, robot, speed, duration):
        super().__init__(robot, duration)
        self.speed = speed

    def execute(self):
        self.robot.run(self.speed)


class Stop(Instruction):
    def execute(self):
        self.robot.stop()


class Rotate(Instruction):
    def __init__(self, robot, speed, angle):
        self.robot = robot
        self.angle = angle
        self.speed = speed

    def execute(self):
        self.robot.rotate(self.speed, self.angle)

    def is_ended(self):
        return True
    
    

