import pigpio
import time
import Constants

def drivetrain_init():
    pi = pigio.pi()
    pi.set_PWM_range(Constants.RANGE)
    pi.set_PWM_frequency(Constants.FREQUENCY)

if not pi.connected:
    exit()

# sparkmax takes pulses between 1000 and 2000 microseconds
# 1000 - 1500 -> reverse
# 1500 - 2000 -> forward
def drive_forward(percent: int):
    pi.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, ((1500 + 500 * percent) / Constants.ConstantsPULSE_LENGTH) * 100)
    pi.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, ((1500 + 500 * percent) / Constants.ConstantsPULSE_LENGTH) * 100)

def turn_left(percent: int):
    pi.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, ((1500 - 500 * percent) / Constants.ConstantsPULSE_LENGTH) * 100)
    pi.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, ((1500 + 500 * percent) / Constants.ConstantsPULSE_LENGTH) * 100)

def turn_right(percent: int):
    pi.set_PWM_dutycycle(Constants.LEFT_DRIVE_PIN, ((1500 + 500 * percent) / Constants.ConstantsPULSE_LENGTH) * 100)
    pi.set_PWM_dutycycle(Constants.RIGHT_DRIVE_PIN, ((1500 - 500 * percent) / Constants.ConstantsPULSE_LENGTH) * 100)

def align_to_tag():
    kp = -0.1
    min_command = 0.05
    