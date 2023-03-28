# import modules
import time
import math
import board
import adafruit_shtc3
import adafruit_mprls
import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
from os import system
import Module1

#establish inputs
i2c = board.I2C()
sht = adafruit_shtc3.SHTC3(i2c)                                         #Delete when humidity sensor is removed
#mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=25)                 #Uncomment when micropressure sensor is attached
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0))

#establish outputs
GPIO.setmode(GPIO.BCM)
outPins = [16, 26]
for i in outPins:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)

#Default VACLimit absent other RPi, equivalent to 300 knots vmo
VACLimit = 1.8
    
#loop
while True:
    #Refresh console output
    system('clear')
    
    #Read from sensor
    temperature, relative_humidity = sht.measurements                   #Delete when humidity sensor is removed
    pitot = 18 #pitot = mpr.pressure                                    #Uncomment when micropressure sensor is attached                                 
    
    #Read from ADC
    stat = mcp.read_adc(0) * 25 / 910
    rho = mcp.read_adc(1) * 2 / 910
    
    #Read VACLimit from other RPi
    VACLimit = 1.8                                                      #Replace with UART poll
    
    #Call module1
    mod1out = Module1.module1(pitot,stat,rho,VACLimit)
    
    #Console debug output
    displayInputs = 1
    if displayInputs:
        print("Temperature: %0.1f C" % temperature)                     #Delete when humidity sensor is removed
        print("Humidity: %0.1f %%" % relative_humidity)                 #Delete when humidity sensor is removed
        print("Pitot: %0.1f PSI" % pitot)
        print("Static: %0.1f PSI" % stat)
        print("Rho: %0.1f PSI" % rho)
        print("VACLimit: %0.1f PSI" % VACLimit)
        print("vmo: %0.1f" % mod1out[2])
    
    #Module1 outputs
    GPIO.output(16,mod1out[1])
    print("Airspeed: %0.1f knots" % mod1out[0])
    if mod1out[1]:
        print("AIRSPEED WARNING")
        
    #Set UART output to mod1out[2]                                      #to do when both RPi are available
    
    #Loop at 0.1 s
    time.sleep(0.1)

