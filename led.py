from gpiozero import LED
import time

led = LED(17)    // connecting GPIO Pin 17 to the LED

// make LED turn on for 1 second and turn off for one sec
while True:
  led.on()
  time.sleep(1)
  led.off
  time.sleep(1)
