import RPi.GPIO as GPIO
import time
import device

# Define the GPIO pins connected to the CD4052 control inputs
S0_PIN = 17  # Example GPIO pin for S0 control
S1_PIN = 18  # Example GPIO pin for S1 control

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(S0_PIN, GPIO.OUT)
GPIO.setup(S1_PIN, GPIO.OUT)


input_str = input("Enter elements separated by spaces: ")
array = input_str.split()  # Split the input string by spaces
# Convert the input elements to the desired data type (e.g., integers)
array = [int(element) for element in array]

def select_channel(channel_number):
    # Convert the channel number to binary and set the control pins accordingly
    GPIO.output(S0_PIN, channel_number & 1)
    GPIO.output(S1_PIN, (channel_number >> 1) & 1)
    #a= channel_number & 1
    #b= (channel_number >> 1) & 1
    

try:
    while True:
        for i in array:
            select_channel(i)
            distance = device.get_distance
            time.sleep(1)
            print("distance:",distance)
            
except KeyboardInterrupt:
    pass

# Clean up GPIO settings before exiting
GPIO.cleanup()