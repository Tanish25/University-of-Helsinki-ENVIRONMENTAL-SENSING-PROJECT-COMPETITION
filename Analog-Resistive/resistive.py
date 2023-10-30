#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import ADS1263
import RPi.GPIO as GPIO

REF = 5.08      			# Modify according to actual voltage

R_k1 = 5000     			# Known resistance-1
R_k2 = 16000    			# Known resistance-2    

GPIO.setwarnings(False)                 # Set GPIO warnings as false
GPIO.setmode(GPIO.BCM)                  # Set the GPIO mode

gpio_pin_10k = 6                  	# Define the GPIO pin you want to use
GPIO.setup(gpio_pin_10k, GPIO.OUT)      # Set the GPIO pin as an output
GPIO.output(gpio_pin_10k, GPIO.HIGH)     # Set GPIO pin - 0 : on; 1 - off

gpio_pin_100k = 5                      	# Define the GPIO pin you want to use
GPIO.setup(gpio_pin_100k, GPIO.OUT)     # Set the GPIO pin as an output
GPIO.output(gpio_pin_100k, GPIO.LOW)   # Set GPIO pin - 0 : on; 1 - off

def CalculateRes(R_known, V_out):
    R_L = R_known/((3.3/V_out) - 1)	# Calculates resistance from voltage(ADC)
    return R_L
    
    
try:
    ADC = ADS1263.ADS1263()		# Initialize ADC
    					# The faster the rate, the worse the stability
    					# and the need to choose a suitable digital filter(REG_MODE1)
    if (ADC.ADS1263_init_ADC1('ADS1263_19200SPS') == -1):
        exit()
    
    ADC.ADS1263_SetMode(0) 		# 0 is singleChannel, 1 is diffChannel
    
    while(1):
        ADC_Value = ADC.ADS1263_GetAll([0, 1, 2])    # get ADC1 value
        x1 = ADC_Value[0] * REF / 0x7fffffff	#5k voltage
        x2 = ADC_Value[1] * REF / 0x7fffffff	#50k voltage
        print("Chn 0 Voltage : " + str(x1))
        print("Chn 1 Voltage : " + str(x2))
        R_1 = CalculateRes(R_k1, x1)
        R_2 = CalculateRes(R_k2, x2)
        print("Chn 0 Resistance : " + str(R_1))
        print("Chn 1 Resistance : " + str(R_2))
        print("\33[5A")
        
    ADC.ADS1263_Exit()

except IOError as e:
    print(e)
   
except KeyboardInterrupt:
    print("ctrl + c:")
    print("Program end")
    ADC.ADS1263_Exit()
    exit()
   
