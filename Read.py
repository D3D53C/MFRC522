#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

ledb= 3
ledr= 5
buz= 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522()



try:
        
        print("PLEASE SHOW YOUR CARD")
        id, reg_no = reader.read()
       
        time.sleep(0.5)

        print(id)

       
        
  

finally:
        GPIO.cleanup()
