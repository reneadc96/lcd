import RPi.GPIO as GPIO
#import BlynkLib
import time
import sys
import lcddriver
import time
import datetime
from time import sleep
import thread
global blynk

GPIO.setmode(GPIO.BOARD)
GPIO.setup(07, GPIO.OUT)
pwm=GPIO.PWM(07, 50)
pwm.start(0)


def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(07, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(07, False)
	pwm.ChangeDutyCycle(0)
	
def long_string(display,text = '',num_line = 1,num_cols = 16):
	if(len(text) > num_cols):
		display.lcd_display_string(text[:num_cols],num_line)
        time.sleep(1)
        for i in range(len(text) - num_cols + 1):
			text_to_print = text[i:i+num_cols]
			display.lcd_display_string(text_to_print,num_line)
			time.sleep(0.2)
			time.sleep(1)
	else:
		display.lcd_display_string(text,num_line)

if __name__== "__main__":
	counter = 1
	down = False
	angle = 0
	
	display = lcddriver.lcd()
	
	while(counter <= 6):
		#if(angle <= 180 ):
			#if(angle == 180):
			#	down = true
			#else if(angle < 180 and down = false):
			#	angle -= 60
			#else:
			#	angle += 60
		
		#else if(angle == 180 and down == true):
		#	angle-= 60	
		if(angle == 180):
			down = True
		elif(angle == 0):
			down = False
		if(down == False):
			angle += 60
		else:
			angle -= 60		 
		SetAngle(angle)
		counter +=1
		
	print("Fido LCD is writing")
    long_string(display,"Next Feed Time 1: ", 1)
    #writing time to display
    display.lcd_display_string(str(datetime.datetime.now().time()), 2)
	pwm.stop()
	GPIO.cleanup()
	
