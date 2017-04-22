#!/usr/bin/env python3
import sys, time, pygame, RPi.GPIO as GPIO  

pygame.init()

# Set up button interfaces
GPIO.setmode(GPIO.BCM)
  
# GPIO 23 & 24 set up as inputs. One pulled up, the other down.  
# 23 will go to GND when button pressed and 24 will go to 3V3 (3.3V)  
# this enables us to demonstrate both rising and falling edge detection  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  


# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def buttonPressA(channel):  
    print("Rising edge detected on port 23")
    print("Layering sample", flush="true")
    pygame.mixer.Sound("/home/pi/dev/samples/looperman-l-1528970-0106359-miesterz-skrillex-ish-growl-whole-thing.wav").play()
    return
    
# now we'll define the threaded callback function  
# this will run in another thread when our event is detected  
def buttonPressB(channel):  
    print("Rising edge detected on port 24")
    print("Layering sample", flush="true")
    pygame.mixer.Sound("/home/pi/dev/samples/looperman-l-2206627-0106476-nadm-world-war-iii.wav").play()
    return
    
  
# The GPIO.add_event_detect() line below set things up so that  
# when a rising edge is detected on port 24, regardless of whatever   
# else is happening in the program, the function "my_callback" will be run  
# It will happen even while the program is waiting for  
# a falling edge on the other button.  
GPIO.add_event_detect(23, GPIO.FALLING, callback=buttonPressA, bouncetime=200)
GPIO.add_event_detect(24, GPIO.FALLING, callback=buttonPressB, bouncetime=200)


print("Starting the music.", flush="true")
pygame.mixer.music.load("/home/pi/dev/samples/Itsy_Bitsy_Spider_Dubstep_New.ogg")
pygame.mixer.music.play()

try:
    var = 1
    while var == 1:
        print("Still running")
        time.sleep(3)
  
except KeyboardInterrupt:  
    print("Stoping the music", flush="true")
    pygame.mixer.music.stop()
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  

print("Bye now.")