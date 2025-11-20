from approxeng.input import CenteredAxis, Controller
import time

def robot_init():
    apriltag_init()

    controller = Controller(
        index=0, # Change if you have multiple controllers
        # Other options depending on connection type
    )

while True:
    # read controller state
    controller.check_presses()
    controller.check_releases()

    

    apriltag_periodic()