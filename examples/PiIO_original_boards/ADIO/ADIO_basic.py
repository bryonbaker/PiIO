#!/usr/bin/python3
#  example usage of PiIO ADIO PCB
#  ==============================
#
#  see https://gpiozero.readthedocs.io/en/stable/recipes.html
#  for info on GPIOZero
#
#  This example does an IO check on the board
#
from gpiozero import PWMLED
from gpiozero import LED 	# in GPIOZero outputs are called LEDs???
from gpiozero import Button
from time import sleep
from PiIO import PiIO_Analog

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 2
 

# @@@@ Hardware init @@@@
#
adc = PiIO_Analog(GAIN)
run = LED(adc.RUN)
PWM1 = PWMLED(adc.PWM1)
PWM2 = PWMLED(adc.PWM2)
IN1 = Button(adc.I1,pull_up=False)
IN2 = Button(adc.I2,pull_up=False)
IN3 = Button(adc.I3,pull_up=False)
IN4 = Button(adc.I4,pull_up=False)
O1 = LED(adc.O1)
O2 = LED(adc.O2)
O3 = LED(adc.O3)
O4 = LED(adc.O4)
O5 = LED(adc.O5)
O6 = LED(adc.O6)
O7 = LED(adc.O7)
O8 = LED(adc.O8)
OE = LED(adc.OE)
# @@@@ Example code here @@@@
#
# attach a LED to Output 6 on the board.
# then PWM at 10Hz, cycle duty cycle then.
#
run.blink(.100,.900)


print("> NOTE - if you experience problems accesing i2C check node red is not also trying to access it")
print("> reading ADC 1..4")
data = .4
for x in range(4):
	for y in range(10):
		data = adc.get_scaled(x) 	
		print (" ",x," scaled ","{:.2f}".format(data),sep='\t',end='')
		data = adc.get_raw(x) 	
		print ("         raw    ",data,sep='\t')
		sleep(.1)

print("> Do rate increase AO1")
for x in range(100):
	PWM1.value = x / 100.0
	sleep(.05)
	print(".",end='',flush=True)
print("")

sleep(2)
print("> Do rate increase AO2")
for x in range(100):
	PWM2.value = x / 100.0
	sleep(.05)
	print(".",end='',flush=True)
print("")


print("> Read temp")
temp = adc.get_temp()
print (" {:.2f}".format(temp)," DegC")

print("> Read DI 1-4")
for x in range(10):
	print(" IN1: ",IN1.is_pressed," IN2: ",IN2.is_pressed," IN3 ",IN3.is_pressed," IN4 ",IN4.is_pressed)
	sleep(1)

print("> DO Output 1..8")
OE.on()
print(" ..1",end='',flush=True)	
O1.on()
sleep(12)
print("..2",end='',flush=True)	
O2.on()
sleep(12)
print("..3",end='',flush=True)	
O3.on()
sleep(12)
print("..4",end='',flush=True)	
O4.on()
sleep(12)
print("..5",end='',flush=True)	
O5.on()
sleep(12)
print("..6",end='',flush=True)	
O6.on()
sleep(12)
print("..7",end='',flush=True)	
O7.on()
sleep(12)
print("..8",end='',flush=True)	
O8.on()
sleep(12)
print("")
print("> wait")
sleep(10)
