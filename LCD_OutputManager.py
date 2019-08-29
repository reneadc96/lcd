# Program used for I2C 16 X 2 Display Fido Project


import lcddriver
import time
import datetime

#load driver to set it as display
display = lcddriver.lcd()
feedTime1 = "08:45:00"
feedTime2 = "21:30:00"
                        
try:
        #long_string function provided by Didac Garcia.
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
    while True:
        #SENTENCES ARE 16 CHARACTERS LONG
        print("Fido LCD is writing")
        long_string(display,"Time Now is: ", 1)
        #writing time to display
        display.lcd_display_string(str(datetime.datetime.now().time()), 2)

        time.sleep(2)
        long_string(display,"Next Feed Time 1: ", 1)
        # writing time to display
        display.lcd_display_string(feedTime1, 2)
   
        time.sleep(3)
        long_string(display,"Next Feed Time 2: ", 1)
        # writing time to display
        display.lcd_display_string(feedTime2, 2)
        time.sleep(3)
        display.lcd_clear()
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()


