import pigpio
from Constants import Constants

class Shooter():

    @staticmethod
    def shooter_init(pigpiod):
        pigpiod.set_mode(Constants.SHOOTER_PIN, pigpio.OUTPUT)
        pigpiod.set_PWM_range(Constants.SHOOTER_PIN, Constants.RANGE)
        Shooter.stop_shooter(pigpiod)

    @staticmethod
    def percent_to_pulse(percentage: float) -> int:
        return ((1500 + 500 * percentage) // Constants.PULSE_LENGTH) * 100

    @staticmethod
    def shoot(pigpiod, percent: float = 0.4):
        pigpiod.set_PWM_dutycycle(Constants.SHOOTER_PIN, Shooter.percent_to_pulse(percent))

    @staticmethod
    def unshoot(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.SHOOTER_PIN, Shooter.percent_to_pulse(-0.2))

    @staticmethod
    def stop_shooter(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.SHOOTER_PIN, Shooter.percent_to_pulse(0))