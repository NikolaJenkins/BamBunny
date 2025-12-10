# from approxeng.input import CenteredAxis, Controller
import evdev
from evdev import InputDevice, categorize, ecodes
import ApriltagDetector
from Drivetrain import Drivetrain
from Intake import Intake
from Shooter import Shooter
import time
import pigpio

pi = pigpio.pi()
device = evdev.InputDevice('/dev/input/event4')

def robot_init():
    # ApriltagDetector.apriltag_init()
    Drivetrain.drivetrain_init(pi)
    Intake.intake_init(pi)
    Shooter.shooter_init(pi)

def test():
    print(device)
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))
    Intake.intake(pi)
    Shooter.shoot(pi)
    time.sleep(5)
    Intake.stop_intake(pi)
    Shooter.stop_shooter(pi)

robot_init()
test()


    # controller = Controller(
    #     index=0, # Change if you have multiple controllers
    #     # Other options depending on connection type
    # )

# while True:
    # read controller state
    # controller.check_presses()
    # controller.check_releases()

    

    # apriltag_periodic()