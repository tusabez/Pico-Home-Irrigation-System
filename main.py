# Import libraries
import time, utime
from machine import Pin, I2C, Timer
from ds3231_i2c import DS3231_I2C

# Set DS I2C ID, SDA, SCL respective pins and uses default frequency (freq=400000)
ds_i2c = I2C(0,sda=Pin(16), scl=Pin(17))
ds = DS3231_I2C(ds_i2c)
# Uncomment the two lines below to set time        0   1   2     3                              4    5    6    
#current_time = b'\x00\x11\x13\x07\x24\x07\x21' # sec\min\hour\week(Sunday = 1 - Saturday = 7)\day\month\year
#ds.set_time(current_time)
# Once time is set, you can delete or recomment the 2 lines above.
# Define the name of week days list. Uncomment if you want to change what days the External LED turns on. Otherwise the current code will turn on every day
#w  = ["Sunday","Monday","Tuesday","Wednesday","Thurday","Friday","Saturday"];

# Set GP25 onboard LED output
led = Pin(25, Pin.OUT)
# Set GP22 as moisture sensor input
moisture = Pin(22,Pin.IN)
# Set GP1 as moisture sensor power relay 2 output
sensor_power = Pin(1,Pin.OUT)
# Set GP0 for water pump relay 1 output
pump = Pin(0,Pin.OUT)
# Set GP2 for external LED relay 3 output
extled = Pin(2, Pin.OUT)
# Watering time in seconds
water = 3
#extled(True)
try:
    sensor_power(True)
    time.sleep(1)
    if moisture.value() == 1:
        pump(True)
        time.sleep(water)
        pump(False)
    sensor_power(False)

    minutes = 60
    hours = 60*minutes
    # Set number of hours in downtime between readings
    downtime = 12*hours
    #Set number of seconds in between powering on and off the onboard led. Useful to visually see if the code is running
    led_cycle = 30

    tim1 = Timer()
    tim2 = Timer()

    def tick(timer):
        sensor_power(True)
        time.sleep(1)
        if moisture.value() == 1:
            pump(True)
            time.sleep(water)
            pump(False)
        sensor_power(False)
    tim1.init(freq=1/downtime, mode=Timer.PERIODIC, callback=tick)

    def LED(timer):
        led(True)
        time.sleep(5)
        led(False)
    tim2.init(freq=1/led_cycle, mode=Timer.PERIODIC, callback=LED)

    while True:
        t = ds.read_time()
        # Replace numbers inside quotation marks with military time to set External LED on and off times
        hour_on = int("7", 16)
        minute_on = int("00", 16)
        hour_off = int("19", 16)
        minute_off = int("00", 16)
        if (t[2]) == hour_on and (t[1]) == minute_on:
            extled(True)
            
        elif (t[2]) == hour_off and (t[1]) == minute_off:
            extled(False)
            
finally:
    led(False)
    extled(False)
    sensor_power(False)
    pump(False)
        
    

    
        




