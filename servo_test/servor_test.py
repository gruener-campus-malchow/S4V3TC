import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)


pwm_frequency = 50 #i.d.R zwischen 40Hz-50Hz (25ms - 20ms)
duty_cycle = 0 #Tastgrad = Impulsdauer/Impulsabstand
pause = 0.5 #seconds
rate = 0.25

# working setup !!!
# pwm_frequency = 50
# duty_cycle = 6.2
# pause = 1
# rate = 0.1


# von 1ms
# 1/20 = 0.05
# 1/25 = 0.04

# Ruhe: 1.5ms
# 1/20 = 0.075
# 1/25 = 0.06

#bis 2ms
# 1/20 = 0.1
# 1/25 = 0.08
p = GPIO.PWM(servoPIN, pwm_frequency) # GPIO 18 als PWM mit 50Hz
p.start(duty_cycle) # Initialisierung
try:
  while True:
    print 'freq=' + str(pwm_frequency) + ' dc=' + str(duty_cycle) + ' wait=' + str(pause)
    time.sleep(pause)
    p.ChangeDutyCycle(duty_cycle)
    duty_cycle = duty_cycle + rate
    
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
