# Pico-Home-Irrigation-System
With this watering system, you can use a Raspberry Pi Pico to water your plants and provide artificial sunlight.
For this project, you'll need a DS3231 RTC module, 3.3v logic 3 channel relay, an LED ring lamp or any other lamp that can run off 5v, a 5v water pump, and a moisture sensor with module. I use a dual USB AC adapter for power.

Connect wires as shown in the diagram
Transfer main.py and ds3231_i2c.py to your raspberry pi pico
Follow instructions in main.py file to run first time clock setup for the DS3231 on lines 10 and 11
Adjust your watering time in seconds on line 27
Adjust how often to check soil wetness in hours on line 41
Adjust your on off times for your lighting under while True loop

I've included Suntime.py as part of the downloadable files but have yet to successfully implement LED lamp on and off times based on local sunrise and sunset times.  If anyone wants to take a crack at it, please be my guest.

I would also like to give credit to www.explainingcomputers.com as the host created similar code for the Raspberry Pi. I took those ideas to create this.
