import pigpio
from Constants import Constants

class Shooter():

    @staticmethod
    def shooter_init(pigpiod):
        pigpiod.set_mode(Constants.UPPER_SHOOTER_PIN, pigpio.OUTPUT)
        pigpiod.set_PWM_range(Constants.UPPER_SHOOTER_PIN, Constants.RANGE)
        pigpiod.set_PWM_frequency(Constants.UPPER_SHOOTER_PIN, Constants.FREQUENCY)
        pigpiod.set_mode(Constants.LOWER_SHOOTER_PIN, pigpio.OUTPUT)
        pigpiod.set_PWM_range(Constants.LOWER_SHOOTER_PIN, Constants.RANGE)
        pigpiod.set_PWM_frequency(Constants.LOWER_SHOOTER_PIN, Constants.FREQUENCY)
        Shooter.stop_shooter(pigpiod)

    @staticmethod
    def percent_to_pulse(percentage: float) -> int:
        return ((1500 + 500 * percentage) // Constants.PULSE_LENGTH) * 100

    @staticmethod
    def shoot(pigpiod, percent: float = 0.4):
        pigpiod.set_PWM_dutycycle(Constants.UPPER_SHOOTER_PIN, Shooter.percent_to_pulse(percent))
        pigpiod.set_PWM_dutycycle(Constants.LOWER_SHOOTER_PIN, Shooter.percent_to_pulse(-percent))

    @staticmethod
    def unshoot(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.UPPER_SHOOTER_PIN, Shooter.percent_to_pulse(-0.2))
        pigpiod.set_PWM_dutycycle(Constants.LOWER_SHOOTER_PIN, Shooter.percent_to_pulse(0.2))

    @staticmethod
    def stop_shooter(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.UPPER_SHOOTER_PIN, Shooter.percent_to_pulse(0))
        pigpiod.set_PWM_dutycycle(Constants.LOWER_SHOOTER_PIN, Shooter.percent_to_pulse(0))