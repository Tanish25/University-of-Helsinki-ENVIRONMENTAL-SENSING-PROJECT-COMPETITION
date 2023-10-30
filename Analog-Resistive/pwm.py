import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin you want to use
# For example, GPIO17 is pin number 11 on the board
gpio_pin = 26

# Set the GPIO pin as an output
GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.setwarnings(False)

# Create a PWM instance with a frequency of 100 Hz
pwm = GPIO.PWM(gpio_pin, 100)

# Start PWM with a duty cycle of 50% (0.0 to 100.0)
pwm.start(50)

try:
    while True:
        # Change the duty cycle (0.0 to 100.0) to change the brightness
        # of the PWM signal
        duty_cycle = float(input("Enter duty cycle (0.0 to 100.0): "))
        pwm.ChangeDutyCycle(duty_cycle)
except KeyboardInterrupt:
    # When you press Ctrl+C, this will clean up and exit
    pwm.stop()
    GPIO.cleanup()
