# from approxeng.input import CenteredAxis, Controller
import evdev
from evdev import InputDevice, categorize, ecodes
# import ApriltagDetector
from Drivetrain import Drivetrain
from Intake import Intake
from Shooter import Shooter
import time
import pigpio

pi = pigpio.pi()
try:
    controller = evdev.InputDevice('/dev/input/event4')
except FileNotFoundError:
    print("Controller not found. Try different file path or reconnect the controller.")
    exit()

# controller input values
buttons = {"a": 305, "b": 306, "y": 307, "x": 304}
bumpers = {"left", 308, "right", 309}

def robot_init():
    # ApriltagDetector.apriltag_init()
    Drivetrain.drivetrain_init(pi)
    Intake.intake_init(pi)
    Shooter.shooter_init(pi)

def test():
    print(controller)
    # for event in controller.read_loop():
    #     if event.type == evdev.ecodes.EV_KEY:
    #         print(evdev.categorize(event))
    Intake.intake(pi)
    Shooter.shoot(pi)
    time.sleep(5)
    Intake.stop_intake(pi)
    Shooter.stop_shooter(pi)

robot_init()
test()
for event in controller.read_loop():
    if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
        key = categorize(event)
        # print(key)
    if event.code == buttons["a"]:
        if event.value == 1:
            print("shooter")
        else:
            print("stop shooting")
    if event.code == buttons["b"]:
        if event.value == 1:
            print("intake")
        else:
            print("stop intaking")
    if event.code == buttons["y"]: 
        if event.value == 1:
            print("outtake")
        else:
            print("stop intaking")
        # if event.code not in buttons[1] or event.code not in bumpers[1]:
        #     print(key.scancode)
# for event in controller.read_loop():
#     if event == 

    # apriltag_periodic()