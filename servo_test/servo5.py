from multiprocessing import Process
import time
import RPi.GPIO as GPIO

def rotate_motor(direction):
   servoPIN = 17
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(servoPIN, GPIO.OUT)
   p = GPIO.PWM(servoPIN, 50) # GPIO 18 als PWM mit 50Hz
   p.start(0) # Initialisierung

   uzs_min = 7.2
   uzs_max = 6.0
   uzs_rate = -0.05

   guzs_min = 7.2
   guzs_max = 8.4
   guzs_rate = 0.05

   dc = 0.0
     
   if direction < 0 :
        try:
           dc = guzs_min
           while dc < guzs_max:
             p.ChangeDutyCycle(dc)
             print 'motor accelerating with dc=' + str(dc)
             time.sleep(0.1)
             dc = dc + guzs_rate
           while True:
             print 'motor running with dc=' + str(dc)
             time.sleep(1)
        except KeyboardInterrupt:
          p.stop()
          GPIO.cleanup()
   elif direction > 0:
        try:
           dc = uzs_min
           while dc > uzs_max:
             p.ChangeDutyCycle(dc)
             print 'motor accelerating with dc=' + str(dc)
             time.sleep(0.1)
             dc = dc + uzs_rate
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

