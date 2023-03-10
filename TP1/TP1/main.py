#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys
from robot import Robot
from instructions import *

robot = Robot(
    left_motor=Motor(Port.B),
    right_motor=Motor(Port.C),
    color_sensor=ColorSensor(Port.S3),
    distance_sensor=None
)

instructions = InstructionSet([
    Forward(robot, speed=500, duration=2),
    Stop(robot, duration=1),
    Rotate(robot, 400, 90),
    Stop(robot, 1),
    Rotate(robot, 400, -90),
    Forward(robot, 400, 4),
    Stop(robot, 10)
])

for instruction in instructions:
    instruction.execute()
    robot.log()


