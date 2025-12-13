# from approxeng.input import CenteredAxis, Controller
import evdev
from evdev import InputDevice, categorize, ecodes
# import ApriltagDetector
from Drivetrain import Drivetrain
from Intake import Intake
from Shooter import Shooter
from Constants import Constants
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
    print(pi.get_PWM_dutycycle(Constants.INTAKE_PIN))
    Intake.intake(pi)
    time.sleep(2)
    print(pi.get_PWM_dutycycle(Constants.INTAKE_PIN))
    Intake.stop_intake(pi)
    # for event in controller.read_loop():
    #     if event.type == evdev.ecodes.EV_KEY:
    #         print(evdev.categorize(event))
    # Intake.intake(pi)
    # Shooter.shoot(pi)
    # time.sleep(5)
    # Intake.stop_intake(pi)
    # Shooter.stop_shooter(pi)

robot_init()
test()
for event in controller.read_loop():
    if event.type == ecodes.EV_KEY:
        key = categorize(event)
        print(key.scancode, key.keystate)
#     # if event.type == ecodes.EV_KEY or event.type == ecodes.EV_ABS:
#         # key = categorize(event)
#         # print(key)
#     if event.code == buttons["a"]:
#         if event.value == 1:
#             # print("shooter")
#             Shooter.shoot(pi, .5)
#             print(pi.get_PWM_dutycycle(Constants.UPPER_SHOOTER_PIN), 
#                   pi.get_PWM_dutycycle(Constants.LOWER_SHOOTER_PIN))
#         else:
#             # print("stop shooting")
#             Shooter.stop_shooter(pi)
#             print(pi.get_PWM_dutycycle(Constants.UPPER_SHOOTER_PIN), 
#                   pi.get_PWM_dutycycle(Constants.LOWER_SHOOTER_PIN))
#     if event.code == buttons["b"]:
#         if event.value == 1:
#             # print("intake")
#             Intake.intake(pi)
#             print(pi.get_PWM_dutycycle(Constants.INTAKE_PIN))
#         else:
#             # print("stop intaking")
#             Intake.stop_intake(pi)
#             print(pi.get_PWM_dutycycle(Constants.INTAKE_PIN))
#     if event.code == buttons["y"]: 
#         if event.value == 1:
#             # print("outtake")
#             Intake.outtake(pi)
#             print(pi.get_PWM_dutycycle(Constants.INTAKE_PIN))
#         else:
#             # print("stop outtaking")
#             Intake.stop_intake(pi)
#             print(pi.get_PWM_dutycycle(Constants.INTAKE_PIN))
#         # if event.code not in buttons[1] or event.code not in bumpers[1]:
#         #     print(key.scancode)
# # for event in controller.read_loop():
#     if event == 

    # apriltag_periodic()