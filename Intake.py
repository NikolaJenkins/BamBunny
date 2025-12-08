from Constants import Constants
import pigpio

class Intake():

    @staticmethod
    def intake_init(pigpiod):
        pigpiod.set_mode(Constants.INTAKE_PIN, pigpio.OUTPUT)
        pigpiod.set_PWM_range(Constants.INTAKE_PIN, Constants.RANGE)
        Intake.stop_intake(pigpiod)

    @staticmethod
    def percent_to_pulse(percentage: float) -> int:
        return ((1500 + 500 * percentage) // Constants.RANGE) * 100
    
    @staticmethod
    def intake(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.INTAKE_PIN, Intake.percent_to_pulse(0.25))

    @staticmethod
    def outtake(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.INTAKE_PIN, Intake.percent_to_pulse(-0.25))

    @staticmethod
    def stop_intake(pigpiod):
        pigpiod.set_PWM_dutycycle(Constants.INTAKE_PIN, Intake.percent_to_pulse(0))