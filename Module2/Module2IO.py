# import modules
import time
import struct
import math
import board
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
from os import system
import Module2

#establish outputs
GPIO.setmode(GPIO.BCM)
outPins = [4,26,24,16]
for i in outPins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)

#establish inputs
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0))
GPIO.setup(18,GPIO.IN)

#Default values
weightDEFAULT = 60000
vacDEFAULT = 1
flapDEFAULT = 0
vmoWarnDEFAULT = 0
overrideDefaults = 1
    
#loop
while True:
    #Refresh console output
    system('clear')
    
    #Read vmoWarn from other RPi
    vmoWarn = GPIO.input(18) if overrideDefaults else vmoWarnDEFAULT
                           
    #Read from ADC
    weight = mcp.read_adc(0) * 70000 / 1024 + 50000 if overrideDefaults else weightDEFAULT
    vac = mcp.read_adc(1) * 6 / 1024 - 2 if overrideDefaults else vacDEFAULT
    flap = mcp.read_adc(2) * 40 / 1024 - 2 if overrideDefaults else flapDEFAULT
    
    #Call module2
    mod2out = Module2.module2(weight,vac,flap,vmoWarn)
    
    #Console output
    print("INPUTS:")
    print("Weight: %0.1f kg" % weight)
    print("Vert. Acceleration: %1f G" % vac)
    print("Flap Position: %0.1f degrees" % flap)
    if vmoWarn:
        print("Airspeed Warning: ON")
    else:
        print("Airspeed Warning: OFF")
    print("")
    print("OUTPUTS:")
    if mod2out[0]:
        print("Vert. Acceleration Warning: ON")
    else:
        print("Vert. Acceleration Warning: OFF")
        
    if mod2out[1]:
        print("Manoeuvre Warning: ON")
    else:
        print("Manoeuvre Warning: OFF")
    
    #LED outputs
    GPIO.output(26,mod2out[0]) #Left light = vacWarn
    GPIO.output(16,mod2out[1]) #Right light = manWarn
    
    #Run at 0.1s intervals
    time.sleep(0.1)

