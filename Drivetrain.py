import pigpio
import time
from Constants import Constants

class Drivetrain():

    @staticmethod
    def drivetrain_init(pigpiod):
        pigpiod.set_mode(Constants.RIGHT_DRIVE_PIN, pigpio.OUTPUT)
        pigpiod.set_mode(Constants.LEFT_DRIVE_PIN, pigpio.OUTPUT)
        pigpiod.set_PWM_range(Constants.RIGHT_DRIVE_PIN, Constants.RANGE)
        pigpiod.set_PWM_range(Constants.LEFT_DRIVE_PIN, Constants.RANGE)
        pigpiod.set_PWM_frequency(Constants.RIGHT_DRIVE_PIN, Constants.FREQUENCY)
        pigpiod.set_PWM_frequency(Constants.LEFT_DRIVE_PIN, Constants.FREQUENCY)
        Drivetrain.stop_driving(pigpiod)

    @staticmethod
    def percent_to_pulse(percentage: float) -> int:
        return ((1500 + 500 * percentage) // Constants.PULSE_LENGTH) * 100

    # sparkmax takes pulses between 1000 and 2000 microseconds
    # 1000 - 1500 -> reverse
    # 1500 - 2000 -> forward
    @staticmethod
    def drive_forward(percent: float, pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, Drivetrain.percent_to_pulse(percent))
        pigpiod.pi.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, Drivetrain.percent_to_pulse(percent))

    @staticmethod
    def turn_left(percent: float, pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, Drivetrain.percent_to_pulse(-percent))
        pigpiod.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, Drivetrain.percent_to_pulse(percent))

    @staticmethod
    def turn_right(percent: float, pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, Drivetrain.percent_to_pulse(percent))
        pigpiod.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, Drivetrain.percent_to_pulse(-percent))

    @staticmethod
    def stop_driving(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, 0)
        pigpiod.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, 0)

    @staticmethod
    def align_to_tag():
        kp = -0.1
        min_command = 0.05