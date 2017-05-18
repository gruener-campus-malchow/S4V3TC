from multiprocessing import Process
import time
import RPi.GPIO as GPIO
import numpy
def rotate_motor(direction):
   servoPIN = 17
   frequency = 50

   GPIO.setmode(GPIO.BCM)
   GPIO.setup(servoPIN, GPIO.OUT)

   p = GPIO.PWM(servoPIN, frequency) # GPIO 18 als PWM mit 50Hz
   p.start(0) # Initialisierung

   acc_rate = 0.1 #sleep in ms - bigger value for slower

# uzs = uhrzeigersinn = clock like
   uzs_min = 7.2
   uzs_max = 6.0
   uzs_rate = -0.05
# guzs = gegen den uhrzeigersinn = counter clock like
   guzs_min = 7.2
   guzs_max = 8.4
   guzs_rate = 0.05
      
   if direction < 0 :
      dc_start = guzs_min
      dc_end = guzs_max
      dc_rate = guzs_rate
   elif direction > 0 :
      dc_start = uzs_min
      dc_end = uzs_max
      dc_rate = uzs_rate

   try:
     dc = dc_start
     while dc in numpy.arange(dc_start, dc_end) :
       p.ChangeDutyCycle(dc)
       print 'motor accelerating with dc=' + str(dc) + ' and dc_rate=' + str(dc_rate)
       time.sleep(acc_rate)
       dc = dc + dc_rate
     while True:
       print 'motor running with dc=' + str(dc)
       time.sleep(1)
   except KeyboardInterrupt:
     p.stop()
     GPIO.cleanup()

if __name__ == '__main__':
   while 1:
      command = raw_input('type: "left" or "right"')
      if command == 'right':
         print 'starting motor if not started yet'
         #if p.is_alive() != 1:
         motor = Process(target=rotate_motor, args=(1,))
         motor.start()
      elif command == 'left':
         motor = Process(target=rotate_motor, args=(-1,))
         motor.start()
      else:
         print 'stopping motor'
         motor.terminate()

